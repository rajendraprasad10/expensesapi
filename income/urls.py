from django.contrib import admin
from django.urls import path, include


from .views import IncomeDetailAPIView, IncomeListAPIView


urlpatterns = [
    path('', IncomeListAPIView.as_view(),name ='incomes' ),
    path('<int:id>', IncomeDetailAPIView.as_view(),name ='income' ),
]