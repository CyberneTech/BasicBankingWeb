from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField()
    class Meta:
        db_table = "Users"


class Transaction(models.Model):
    sender = models.ForeignKey(Users, on_delete = models.CASCADE)
    receiver = models.ForeignKey(Users, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    amt = models.DecimalField()
    class Meta:
        db_table = "Transaction"