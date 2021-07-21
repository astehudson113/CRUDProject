from django.db import models


# Create your models here.  
class Employee(models.Model):
     eid=models.IntegerField()
     ename=models.CharField(max_length=30)
     email=models.EmailField(max_length=50)
     ephno=models.CharField(max_length=15)
     eexp=models.FloatField()
     edob=models.DateField()
     esal=models.IntegerField()
     def __str__(self):
      return str(self.ename)

