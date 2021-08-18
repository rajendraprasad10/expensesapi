from .views import ExpenseSummary
from django.urls import path


urlpatterns = [
    path('expense_category_data', ExpenseSummary.as_view(), name='expese-cotegory-summary')
]
