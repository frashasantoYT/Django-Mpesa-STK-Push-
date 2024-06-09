from django.db import models

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=50, unique=True)
    amount = models.FloatField()
    phone_number = models.CharField(max_length=20)
    account_reference = models.CharField(max_length=50)
    transaction_desc = models.CharField(max_length=255)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id
