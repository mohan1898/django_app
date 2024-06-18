from django.db import models

class StudenInfo(models.Model):
    name=models.CharField(max_length=40)
    branch=models.CharField(max_length=40)
    rollno=models.IntegerField()

    def __str__(self):
        return self.name


