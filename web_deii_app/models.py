import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class Faq(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, blank=False, null=False)
    question = models.CharField(max_length=255, blank=False, null=False)
    answer = models.TextField(max_length=2048)

    def __str__(self):
        return self.question
