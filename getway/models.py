from os import access
from django.db import models
from users.models import User
# Create your models here.

class Jwt(models.Model):
    user = models.ForeignKey(User, related_name="login_user", on_delete=models.CASCADE)
    access = models.TextField()
    refresh = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now=True)