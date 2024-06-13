from django.db import models, transaction
from django.contrib.auth.models import User
from django.db.models import Sum, Q, Count
from django.db.models.functions import Coalesce


class Transaction(models.Model):
    CHARGE = 1
    PURCHASE = 2
    TRANSFER_RECEIVED = 3
    TRANSFER_SENT = 4

    transaction_type_choices = (
        (CHARGE, 'CHARGE'),
        (PURCHASE, 'PURCHASE'),
        (TRANSFER_RECEIVED, 'TRANSFER_RECEIVED'),
        (TRANSFER_SENT, 'TRANSFER_SENT')
    )

    user = models.ForeignKey(User, related_name='transactions', on_delete=models.RESTRICT)
    transaction_type = models.PositiveSmallIntegerField(choices=transaction_type_choices, default=CHARGE)
    amount = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.transaction_type} - {self.amount}'

    @classmethod
    def get_report(cls):
        """show all users and their balances"""
        positive_transaction = Sum('transactions__amount', filter=Q(transactions__transaction_type__in=[1, 3]))
        negative_transaction = Sum('transactions__amount', filter=Q(transactions__transaction_type__in=[2, 4]))
        users = User.objects.all().annotate(transactions_count=Count('transactions__id'),
                                            balance=Coalesce(positive_transaction, 0) - Coalesce(negative_transaction,
                                                                                                 0))
        return users

    @classmethod
    def get_total_balance(cls):
        queryset = cls.get_report()
        return queryset.aggregate(sum('balance'))

    @classmethod
    def user_balance(cls, user):
        positive_transaction = Sum('amount', filter=Q(transactions__transaction_type__in=[1, 3]))
        negative_transaction = Sum('amount', filter=Q(transactions__transaction_type__in=[2, 4]))
        user_balance = user.transactions.all().aggregate(
            balance=Coalesce(positive_transaction, 0) - Coalesce(negative_transaction, 0)
        )
        return user_balance.get('balance', 0)


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balance_record')
    balance = models.BigIntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.balance} - {self.created_time}'

    @classmethod
    def record_user_balance(cls, user):
        balance = Transaction.user_balance(user)
        instance = cls.objects.create(user=user, balance=balance)
        return instance

    @classmethod
    def record_all_user_balance(cls):
        for user in User.objects.all():
            cls.record_user_balance(user)


class TransferTransaction(models.Model):
    sender_transaction = models.OneToOneField(Transaction, related_name='sent_transfer', on_delete=models.RESTRICT)
    receiver_transaction = models.OneToOneField(Transaction, related_name='receive_transfer', on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.sender_transaction} >> {self.receiver_transaction}"

    @classmethod
    def transfer(cls, sender, receiver, amount):
        if Transaction.user_balance(sender) < amount:
            return "Transaction not allowed, insufficient balance"

        with transaction.atomic():
            sender_transaction = Transaction.objects.create(
                user=sender, amount=amount, transaction_type=Transaction.TRANSFER_SENT
            )

            receiver_transaction = Transaction.object.create(
                user=receiver, amount=amount, transaction_type=Transaction.TRANSFER_RECEIVED
            )

            instance = cls.objectc.create(
                sender_transaction=sender_transaction, receiver_transaction=receiver_transaction
            )
            return instance


class UserScore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()

    @classmethod
    def change_score(cls, user, score):
        instance = cls.objects.select_for_update().get(user=user)
        with transaction.atomic():
            if not instance.exists():
                instance = cls.objects.create(user=user, score=0)
            else:
                instance = instance.first()
            instance.score += score
            instance.save()
