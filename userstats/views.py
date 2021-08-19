from django.shortcuts import render
from rest_framework.views import APIView
import datetime
from expenses.models import Expenses
from income.models import Income
from rest_framework import status, response



class ExpenseSummary(APIView):
    
    def get_amount_for_category(self, expense_list, category):
        expenses = expense_list.filter(category=category)
        amount = 0

        for expense in expenses:
            amount+= expense.amount

        return {"amount": str(amount)}
    
    def get_category(self, expense):
        return expense.category

    def get(self, request):
        todays_date = datetime.date.today()
        ayear_ago = todays_date-datetime.timedelta(days=30*12)
        expenses = Expenses.objects.filter(
            owner=request.user, date__gte=ayear_ago, date__lte=todays_date
        )

        final = {}
        categories = list(set(map(self.get_category, expenses)))

        for expense in expenses:
            for category in categories:
                final[category] = self.get_amount_for_category(
                    expenses, category
                )

        return response.Response({"category_data": final}, status=status.HTTP_200_OK)



class IncomeSummary(APIView):
    
    def get_amount_for_source(self, income_list, source):
        incomes = income_list.filter(source=source)
        amount = 0

        for income in incomes:
            amount+= income.amount

        return {"amount": str(amount)}
    
    def get_source(self, income):
        return income.source

    def get(self, request):
        todays_date = datetime.date.today()
        ayear_ago = todays_date-datetime.timedelta(days=30*12)
        incomes = Income.objects.filter(
            owner=request.user, date__gte=ayear_ago, date__lte=todays_date
        )

        final = {}
        sources = list(set(map(self.get_source, incomes)))

        for i in incomes:
            for source in sources:
                final[source] = self.get_amount_for_source(
                    incomes, source
                )

        return response.Response({"Income_source_data": final}, status=status.HTTP_200_OK)