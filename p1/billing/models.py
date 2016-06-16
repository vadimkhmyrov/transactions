from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import decimal

class Account(models.Model):
	name = models.CharField(max_length=512)
	debit = models.DecimalField(default=0, max_digits=18, decimal_places=6)
	credit = models.DecimalField(default=0, max_digits=18, decimal_places=6)

	def __str__(self):
		return self.name

	def get_balance(self):
		b = self.debit - self.credit
		return b

class AccountingTransaction(models.Model):
	created = models.DateTimeField(default=datetime.now)
	amount = models.DecimalField(default=0, max_digits=16, decimal_places=6)
	debit = models.ForeignKey(Account, related_name='debit_transactions')
	credit = models.ForeignKey(Account, related_name='credit_transactions')
	status = models.BooleanField(default=False) #True=success, False=fail

	def __str__(self):
		r = 'Transaction between %s and %s on %s'%(self.credit.name, self.debit.name, str(self.created))
		return r

	def save(self, *args, **kwargs):
		if self.credit.get_balance() >= self.amount:

			self.status = True

			C = Account.objects.get(name=self.credit.name)
			D = Account.objects.get(name=self.debit.name)

			C.credit+=decimal.Decimal(self.amount)
			D.debit+=decimal.Decimal(self.amount)

			C.save()
			D.save()
			
		else:
			print 'Error:',self.credit.name,'has insufficient balance for this purchase.'

		super(AccountingTransaction, self).save(*args, **kwargs)