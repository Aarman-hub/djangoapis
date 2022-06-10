from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError("Email field is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save();
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('username',"admin")

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")


        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(name="username", unique=True, max_length=50)
    first_name = models.CharField(name="First name", max_length=255, null=True, blank=True)
    last_name = models.CharField(name="Last name", max_length=255, null=True, blank=True)
    dob = models.DateTimeField(name="Dath of Birth", blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True);
    date_joined = models.DateTimeField(name="Joined Date", auto_now_add=True, auto_now=False)



    USERNAME_FIELD = "email";
    REQUIRED_FIELDS: ('username')

    objects = UserManager();


    def __str__(self):
        return self.email;