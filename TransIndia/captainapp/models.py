from django.db import models
import email
from django.forms import CharField, ImageField

# Create your models here.

# captain registration backend start

class CaptainModel(models.Model):
    cap_id=models.AutoField(primary_key=True)
    cap_name=models.CharField(max_length=100)
    cap_mobile=models.BigIntegerField()
    cap_email=models.EmailField(max_length=100)
    city=models.CharField(max_length=100)
    cap_vehicle=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    con_pwd=models.CharField(max_length=100)
    status=models.CharField(default='pending',null=True,max_length=100)

    class Meta:
        db_table= 'captain_details'

# Captain registration backens ends.
