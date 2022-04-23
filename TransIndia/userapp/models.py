from django.db import models
import email
from django.forms import CharField, ImageField



# Create your models here.

# user registration backend starts

class UserModel(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100)
    user_mobile=models.BigIntegerField()
    user_email=models.EmailField(max_length=100)
    pwd=models.CharField(max_length=100)
    con_pwd=models.CharField(max_length=100)
    user_reg_date=models.DateField(auto_now=True)
    status=models.CharField(default='pending',max_length=100,null=True)

    class Meta:
        db_table= 'user_details'

# user registration backend ends.
