from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import IncomeSerializer
from .permissions import IsOwner
from .models import Income
from rest_framework import permissions

class IncomeListAPIView(ListCreateAPIView):
    serializer_class=IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = [permissions.IsAuthenticated,]


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwner, ]
    lookup_field = 'id'
        
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)