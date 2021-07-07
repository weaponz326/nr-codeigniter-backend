from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Report, ReportAssessment, ReportStudent
from module_students.models import Student
from module_assessment.models import AssessmentSheet
from .serializers import (
    ReportSerializer, 
    ReportAssessmentSerializer, 
    ReportStudentListSerializer
)
from module_assessment.serializers import AssessmentSheetSerializer, AssessmentSheetListSerializer


# Create your views here.

class ReportView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        report = Report.objects.filter(account=account)
        serializer = ReportSerializer(report, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ReportDetailView(APIView):
    def get(self, request, pk, format=None):
        report = Report.objects.get(pk=pk)
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        report = Report.objects.get(pk=pk)
        serializer = ReportSerializer(report, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        report = Report.objects.get(pk=pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------------------------------------------
# class report sheet and assessments 
class ReportAssessmentView(APIView):
    def get(self, request, format=None):
        report = self.request.query_params.get('report', None)
        report_assessment = ReportAssessment.objects.filter(report=report)
        serializer = ReportAssessmentSerializer(report_assessment, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReportAssessmentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class RefreshSheetView(APIView):
    def get(self, request, format=None):
        report_id = self.request.query_params.get('report', None)
        report = Report.objects.get(id=report_id)
        class_id = report.clas.id
        student_set = Student.objects.filter(clas=class_id)

        student_list = []

        if student_set.exists():
            for student in student_set.iterator():
                this_student = ReportStudent.objects.filter(student=student.id)
                if not this_student.exists():
                    student_list.append(ReportStudent(report=report, student=student))
            if not student_list == []: ReportStudent.objects.bulk_create(student_list)

        return Response({ 'message' : 'OK' })

class ClassReportStudentView(APIView):
    def get(self, request, format=None):
        report = self.request.query_params.get('report', None)
        report_student = ReportStudent.objects.filter(report=report)
        serializer = ReportStudentListSerializer(report_student, many=True)        
        return Response(serializer.data)

class ClassAssessmentSheetView(APIView):
    def get(self, request, format=None):
        report = self.request.query_params.get('report', None)
        assessment_set = ReportAssessment.objects.filter(report=report)
        
        sheet_data = []

        if assessment_set.exists():
            for assessment in assessment_set.iterator():
                assessment_sheet = AssessmentSheet.objects.filter(assessment=assessment.assessment)
                serializer = AssessmentSheetSerializer(assessment_sheet, many=True)        
                sheet_data.append(serializer.data)

        return Response(sheet_data)

# -------------------------------------------------------------------------------------------------------
# student report 

class StudentReportView(APIView):
    def get(self, request, format=None):
        student = self.request.query_params.get('student', None)
        report_student = ReportStudent.objects.get(student=student)
        serializer = ReportStudentListSerializer(report_student)        
        return Response(serializer.data)

class StudentAssessmentSheetView(APIView):
    def get(self, request, format=None):
        report = self.request.query_params.get('report', None)
        student = self.request.query_params.get('student', None)
        assessment_set = ReportAssessment.objects.filter(report=report)
        
        sheet_data = []

        if assessment_set.exists():
            for assessment in assessment_set.iterator():
                this_assessment = AssessmentSheet.objects.get(assessment=assessment.assessment)  
                serializer = AssessmentSheetListSerializer(this_assessment)        
                sheet_data.append(serializer.data)
        
        return Response(sheet_data)
