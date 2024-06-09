from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    CHARGE = 1
    PURCHASE = 2
    TRANSFER = 3

    transaction_type_choices = (
        (CHARGE,'CHARGE'),
        (PURCHASE, 'PURCHASE'),
        (TRANSFER, 'TRANSFER')
    )

    user = models.ForeignKey(User, related_name='transactions', on_delete=models.RESTRICT)
    transaction_type = models.PositiveSmallIntegerField(choices=transaction_type_choices, default=CHARGE)
    amount = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.transaction_type} - {self.amount}'


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balance_record')
    balance = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.balance} - {self.created_time}'


# t = Transaction(user_id=2, transaction_type=1, amount=3000, created_time="2024-06-09 09:37:22.886729+03:30")
# t.save()

