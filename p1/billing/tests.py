from django.test import TestCase
from .models import AccountingTransaction, Account

class TransactionTest(TestCase):

	def setUp(self):
		Account.objects.create(name='test_creditor', debit=10.000000, credit=0.000000)
		Account.objects.create(name='test_debitor', debit=0.000000, credit=0.000000)

	def test_transaction_success(self):
		creditor = Account.objects.get(name='test_creditor')
		debitor = Account.objects.get(name='test_debitor')
		AccountingTransaction.objects.create(debit=debitor,credit=creditor,amount=5.000000)
		t = AccountingTransaction.objects.get(debit=debitor,credit=creditor)
		self.assertTrue(t.status)

	def test_transaction_fail(self):
		creditor = Account.objects.get(name='test_creditor')
		debitor = Account.objects.get(name='test_debitor')
		AccountingTransaction.objects.create(debit=creditor,credit=debitor,amount=5.000000)
		t = AccountingTransaction.objects.get(debit=creditor,credit=debitor)
		self.assertFalse(t.status)