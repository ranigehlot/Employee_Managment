from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    mobile=models.CharField(max_length=12,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    city=models.CharField(max_length=200)
    salary=models.FloatField()
    
    class Meta: 
        db_table="empdata"
    
