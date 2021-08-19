from .views import ExpenseSummary, IncomeSummary
from django.urls import path


urlpatterns = [
    path('expense_category_data', ExpenseSummary.as_view(), name='expese-cotegory-summary'),
    path('income_sources_data', IncomeSummary().as_view(), name='income-sources-summary'),

]
