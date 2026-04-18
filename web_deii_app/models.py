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
    email = models.CharField(unique=True, max_length=255, blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_comunicacion = models.BooleanField(default=False)
    is_estudios = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'user'

    objects = UserManager()

    def __str__(self):
        return self.email

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    degree = models.CharField(max_length=255, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    semester = models.IntegerField(blank=False, null=False)
    area = models.CharField(max_length=255, blank=False, null=False)


def file_path(instance, filename):
    return "{0}/{1}".format(instance.subject_id, filename) # id_de_asignatura/archivo

class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

class File(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.ManyToManyField(Subject, related_name='files_id', blank=False)
    uploader = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to=file_path, blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=False)
    approver_id = models.ForeignKey('User', related_name='files_id', on_delete=models.SET_NULL, null=True)
    publish_date = models.DateField(null=True)
    tags = models.ManyToManyField('Tag', related_name='files_id', blank=True)


class NewsPost(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('User', related_name='posts_id', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    publish_date = models.DateField(blank=False, null=False)
    edited_date = models.DateField(null=True)


class Faq(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, blank=False, null=False)
    question = models.CharField(max_length=255, blank=False, null=False)
    answer = models.TextField(max_length=2048)
