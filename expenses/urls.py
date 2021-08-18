from django.contrib import admin
from django.urls import path, include


from .views import ExpenseDetailAPIView, ExpenseListAPIView


urlpatterns = [
    path('', ExpenseListAPIView.as_view(),name ='expenses' ),
    path('<int:id>', ExpenseDetailAPIView.as_view(),name ='expense' ),


]