from django.shortcuts import render
from django.db.models.aggregates import Sum

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Fee, FeesItem, ArrearsItem, TargetClass, Bill
from module_classes.models import Class
from module_payments.models import Payment
from module_students.models import Student
from .serializers import (
    FeeSerializer, 
    FeesItemSerializer, 
    ArrearsItemSerializer, 
    TargetClassSerializer,
    BillSerializer
)


# Create your views here.

class FeeView(APIView):
    def get(self, request, format=None):
        account = self.request.query_params.get('account', None)
        fee = Fee.objects.filter(account=account)
        serializer = FeeSerializer(fee, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class FeeDetailView(APIView):
    def get(self, request, pk, format=None):
        fee = Fee.objects.get(pk=pk)
        serializer = FeeSerializer(fee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        fee = Fee.objects.get(pk=pk)
        serializer = FeeSerializer(fee, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        fee = Fee.objects.get(pk=pk)
        fee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# target classes

class TargetClassView(APIView):
    def get(self, request, format=None):
        fee = self.request.query_params.get('fee', None)
        target_class = TargetClass.objects.filter(fee=fee)
        serializer = TargetClassSerializer(target_class, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TargetClassSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class TargetClassDetailView(APIView):

    def delete(self, request, pk, format=None):
        fee = TargetClass.objects.get(pk=pk)
        fee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------------------

# fees item

class FeesItemView(APIView):
    def get(self, request, format=None):
        fee = self.request.query_params.get('fee', None)
        item = FeesItem.objects.filter(fee=fee)
        serializer = FeesItemSerializer(item, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeesItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class FeesItemDetailView(APIView):
    def get(self, request, pk, format=None):
        item = FeesItem.objects.get(pk=pk)
        serializer = FeesItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = FeesItem.objects.get(pk=pk)
        serializer = FeesItemSerializer(item, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        item = FeesItem.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# arrears item

class ArrearsItemView(APIView):
    def get(self, request, format=None):
        fee = self.request.query_params.get('fee', None)
        arrears = ArrearsItem.objects.filter(fee=fee)
        serializer = ArrearsItemSerializer(arrears, many=True)        
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArrearsItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

class ArrearsItemDetailView(APIView):
    def get(self, request, pk, format=None):
        arrears = ArrearsItem.objects.get(pk=pk)
        serializer = ArrearsItemSerializer(arrears)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        arrears = ArrearsItem.objects.get(pk=pk)
        serializer = ArrearsItemSerializer(arrears, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({ 'message': 'OK', 'data': serializer.data })
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        arrears = ArrearsItem.objects.get(pk=pk)
        arrears.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------------------------------------------------
# bills
class GenerateBillView(APIView):
    def get(self, request, format=None):
        
        def calculate_student_bill(fee, student):
            # get all arrears source of fees
            arrears_set = ArrearsItem.objects.filter(fee=fee)
            arrears_amounts = []

            if arrears_set.exists():
                for arrears in arrears_set.iterator():
                    arrears_source = Fee.objects.get(id=arrears.source)

                    # get amount due of payment of source
                    bill_payment = Payment.objects.get(bill__fee=arrears_source, bill__student=student) 
                    arrears_amounts.append(bill_payment.amount_due)

            # calculate sum of all amount due
            total_arrears = 0
            if not arrears_amounts == []:
                for amount in arrears_amounts:
                    total_arrears += amount

            total_fees = FeesItem.objects.filter(fee=fee).aggregate(Sum('amount'))
            total_fees = total_fees['amount__sum']

            total_bill = total_fees + total_arrears
            return total_bill

        fee = self.request.query_params.get('fee', None)
        fee_instance = Fee.objects.get(id=fee)
        target_class_set = TargetClass.objects.filter(fee=fee)
        bill_set = Bill.objects.filter(fee=fee)
        
        create_list = []
        update_list = []

        if target_class_set.exists():
            print('target class is there')
            for target_class in target_class_set.iterator():
                student_set = Student.objects.filter(clas=target_class.id)
                
                for student in student_set.iterator():
                    amount = calculate_student_bill(fee_instance, student)

                    if bill_set.exists():
                        for bill in bill_set.iterator():
                            if bill.student == student:
                                this_bill = Bill.objects.get(id=bill.id)
                                this_bill.amount = amount
                                update_list.append(this_bill)
                            else:
                                create_list.append(Bill(fee=fee_instance, student=student, amount=amount))
                    else:
                        create_list.append(Bill(fee=fee_instance, student=student, amount=amount))

        if not create_list == []: Bill.objects.bulk_create(create_list)
        if not update_list == []: Bill.objects.bulk_update(update_list, ['amount'])

        return Response({ 'message': 'OK' })

class BillView(APIView):
    def get(self, request, format=None):
        fee = self.request.query_params.get('fee', None)
        bill = Bill.objects.filter(fee=fee)
        serializer = BillSerializer(bill, many=True)        
        return Response(serializer.data)

class BillDetailView(APIView):
    def get(self, request, pk, format=None):
        bill = Bill.objects.get(pk=pk)
        serializer = BillSerializer(bill)
        return Response(serializer.data)

# all bills belonging to student
class StudentBillView(APIView):
    def get(self, request, format=None):
        student = self.request.query_params.get('student', None)
        bill = Bill.objects.filter(student=student)
        serializer = BillSerializer(bill, many=True)        
        return Response(serializer.data)

class BillArrearsView(APIView):
    def get(self, request, format=None):
        bill = self.request.query_params.get('bill', None)
        bill_instance = Bill.objects.get(id=bill)
        fee = bill_instance.fee
        student = bill_instance.student

        arrears_set = ArrearsItem.objects.filter(fee=fee)
        arrears_data = []

        if arrears_set.exists():
            for arrears in arrears_set.iterator():
                arrears_source = Fee.objects.get(id=arrears.source)
                bill_payment = Payment.objects.get(bill__fee=arrears_source, bill__student=student) 
                arrears_data.append({ 'item': arrears.item, 'amount': bill_payment.amount_due })

        return Response(arrears_data)
