from django.shortcuts import render
from .models import AccountingTransaction, Account

def main_view(request):
	accounts = Account.objects.all()
	transactions = AccountingTransaction.objects.all()
	template = 'billing/main.html'
	context = {'accounts':accounts,
			   'transactions':transactions}
	return render(request,template,context)