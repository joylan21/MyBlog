from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="images")
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=180)
    created_at=models.DateTimeField(auto_now=True)