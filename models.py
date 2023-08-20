from django.db import models

# Create your models here.
class Employe(models.Model):
    name=models.CharField(max_length=50)
    salary=models.IntegerField()
    dept=models.CharField(max_length=50)
    role=models.CharField( max_length=50)
    def __str__(self):
        return (str(self.id)+'->'+ self.name +"->"+ self.dept+"->" + self.role)
