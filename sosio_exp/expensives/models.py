from django.db import models

# Create your models here.
class friendsInfo(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10,primary_key=True)

class moneyInfo(models.Model):
    name=models.CharField(max_length=50)
    expensive=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateField()
    purpose=models.CharField(max_length=50)