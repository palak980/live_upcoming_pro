from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
from uuid import uuid4
from django.conf import settings

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):

    ADMIN = 1
    STAFF = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STAFF, 'Staff'),
        (USER, 'User')
    )

    
    uid = models.UUIDField(unique=True, editable=False, default=uuid4)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)
    is_admin = models.BooleanField('Is_admin', default=False)
    is_staff = models.BooleanField('Is_staff', default=False)
    is_user = models.BooleanField('Is_user', default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        swappable = 'AUTH_USER_MODEL'