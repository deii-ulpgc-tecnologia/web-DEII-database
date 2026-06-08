import os

from django.db import models
from django.conf import settings
from .validators import file_size_by_category_validator, extension_whitelist_validator
import uuid

def pending_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"pending/{instance.id}.{ext}"

def approved_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"approved/{instance.id}.{ext}"

def denied_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f"denied/{instance.id}.{ext}"

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    subject_id = models.ManyToManyField('subjects_app.Subject', related_name='files', blank=False)
    uploader = models.EmailField(max_length=255, blank=False, null=False)
    file = models.FileField(
        upload_to=pending_upload_path,
        blank=False,
        null=False,
        unique=True,
        validators=[file_size_by_category_validator,extension_whitelist_validator]
    )
    is_active = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='approved_files',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    approved_at = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='tagged_files', blank=True)

    @property
    def extension(self):
        return (os.path.splitext(self.file.name)[1]).replace('.', '')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name