from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=200)
    acc_det = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user_name
    

class AccountDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Bank_Account = models.CharField(max_length = 200)
    Bank_Balance = models.IntegerField(default = 0)    
    
class Transac(models.Model):
    transac = models.ForeignKey(AccountDetails, on_delete=models.DO_NOTHING)
    Last_Transaction = models.CharField(max_length = 200)
    Last_Transaction_Date = models.DateTimeField('Last Transaction On')    
    
    
       

    