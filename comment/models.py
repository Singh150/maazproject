from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class comment(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    description=models.TextField()
    contact=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
   # user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)