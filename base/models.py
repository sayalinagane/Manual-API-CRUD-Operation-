from django.db import models

# Create your models here.

class StudentModel(models.Model):
    sname=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
    course=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.sname},{self.rollno},{self.course}"

