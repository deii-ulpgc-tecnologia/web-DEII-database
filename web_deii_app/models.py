import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, is_comunicacion=False, is_estudios=False, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio.')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_comunicacion=is_comunicacion,
            is_estudios=is_estudios,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_comunicacion', True)
        extra_fields.setdefault('is_estudios', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(unique=True, max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_comunicacion = models.BooleanField(default=False)
    is_estudios = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'user'

    objects = UserManager()

    def __str__(self):
        return self.email

class Faq(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, blank=False, null=False)
    question = models.CharField(max_length=255, blank=False, null=False)
    answer = models.TextField(max_length=2048)

    def __str__(self):
        return self.question

# Dummy to avoid breaking old migrations. Crashes if removed
def file_path(instance, filename):
    return filename

def pending_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"pending/{instance.id}.{ext}"

def approved_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"approved/{instance.id}.{ext}"

def denied_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"denied/{instance.id}.{ext}"