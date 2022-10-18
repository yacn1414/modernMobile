
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    phone = models.IntegerField()


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.phone
