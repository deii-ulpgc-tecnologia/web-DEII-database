from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
import uuid

# Create your models here.
class User(AbstractUser,PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )