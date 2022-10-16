from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Teacher(models.Model):
    name = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    age = models.IntegerField()
    pict = models.FileField(upload_to='app/img')

    def __str__ (self):
        return self.name.username