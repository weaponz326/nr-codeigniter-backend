from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins

from accounts.models import Profile
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer, UserTransactionSerializer


# Create your views here.

class AccountView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AccountSerializer
        queryset = Account.objects.all()

        return Response(queryset)

    def post(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            account = Account(
                user=Profile.objects.get(id=request.data.get("enterprise_id")),
                account_name=request.data.get("account_name"),
                account_number=request.data.get("account_number"),
                bank_name=request.data.get("bank_name")
            )
            account.save()
            latest_account = Account.objects.latest("id")

            return Response({
                'status': True,
                'account_id': latest_account.id
            })
        else:
            return Response({ 'status': False })

class AccountListView(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset = Account.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

class AccountDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# transactions

class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        account = self.request.query_params.get('account', None)
        if account is not None:
            queryset = queryset.filter(account=account)
        return queryset

class TransactionView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TransactionDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# all transactions
class AllTransactionsView(generics.ListAPIView):
    serializer_class = UserTransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(account__user=user)
        return queryset
