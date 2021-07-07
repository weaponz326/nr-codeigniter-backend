from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Assessment, AssessmentSheet
from .serializers import AssessmentSerializer, AssessmentSheetSerializer, AssessmentSheetListSerializer
from module_students.models import Student


# Create your views here.

class AssessmentView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        assessment = Assessment.objects.filter(account=account)
        serializer = AssessmentSerializer(assessment, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssessmentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class AssessmentDetailView(APIView):
    def get(self, request, pk, format=None):
        assessment = Assessment.objects.get(pk=pk)
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        assessment = Assessment.objects.get(pk=pk)
        serializer = AssessmentSerializer(assessment, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        assessment = Assessment.objects.get(pk=pk)
        assessment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# sheet
# ----------------------------------------------------------------------------------------------------------

class RefreshSheetView(APIView):
    def get(self, request, format=None):
        assessment_id = self.request.query_params.get('assessment', None)
        assessment = Assessment.objects.get(id=assessment_id)
        class_id = assessment.clas.id
        student_set = Student.objects.filter(clas=class_id)

        student_list = []

        if student_set.exists():
            for student in student_set.iterator():
                this_student = AssessmentSheet.objects.filter(student=student.id)
                if not this_student.exists():
                    student_list.append(AssessmentSheet(assessment=assessment, student=student))
            if not student_list == []: AssessmentSheet.objects.bulk_create(student_list)

        return Response({ 'message' : 'OK' })

class ClassSheetView(APIView):
    def get(self, request, format=None):
        assessment = self.request.query_params.get('assessment', None)
        sheet = AssessmentSheet.objects.filter(assessment=assessment)
        serializer = AssessmentSheetListSerializer(sheet, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        assessment_sheet=request.data
        assessment_list = []

        for x in assessment_sheet:
            sheet = AssessmentSheet.objects.get(id=x['id'])
            sheet.score=x['score']
            sheet.grade=x['grade']
            sheet.remarks=x['remarks']
            assessment_list.append(sheet)

        AssessmentSheet.objects.bulk_update(assessment_list, ['score', 'grade', 'remarks'])
        return Response({ 'message': 'OK' })
