from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

BLOOD_GROUP_CHOICES = [
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
]

DOCUMENT_CHOICES = [
    ("Voter ID", "Voter ID"),
    ("Passport", "Passport"),
    ("Citizenship Number", "Citizenship Number"),
]


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")
        
        return self._create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=225, unique=True)
    first_name = models.CharField(max_length=225, blank=True, null=True)
    middle_name = models.CharField(max_length=225, blank=True, null=True)
    last_name = models.CharField(max_length=225, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True, help_text="YYYY-MM-DD")
    gender = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])
    blood_group = models.CharField(max_length=3, blank=True, null=True, choices=BLOOD_GROUP_CHOICES)
    identity_document_type = models.CharField(max_length=225, choices=DOCUMENT_CHOICES, null=True, blank=True)
    identity_document_number = models.CharField(max_length=225, null=True, blank=True)
    photo = models.ImageField(upload_to="profileImage/", null=True, default='profileImage/default_pic.jpg')
    get_joined = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    is_email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return f"{self.first_name} {self.middle_name if self.middle_name else '' } {self.last_name if self.last_name else ''}"
    
    objects = UserManager()
    

