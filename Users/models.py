
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserCustom(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    state = models.CharField(max_length=50)
    phone = models.IntegerField()


    def __str__(self):
        return self.state

    def __unicode__(self):
        return self.user
