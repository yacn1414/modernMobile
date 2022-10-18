from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class comment(models.Model):
    text = models.TextField()
    user_id = models.IntegerField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    Product_id = models.IntegerField()

    def __str__(self):
        return str(self.username)

