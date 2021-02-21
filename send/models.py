from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    class Meta:
        db_table = "Users"
    
    def __str__(self):
        return self.name


class Transaction(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    amt = models.IntegerField()
    class Meta:
        db_table = "Transaction"

    def __str__(self):
        return (self.sender+' '+self.receiver)

    