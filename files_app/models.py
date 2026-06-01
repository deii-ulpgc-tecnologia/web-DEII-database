from django.db import models
import uuid

# Create your models here.
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

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    subject_id = models.ManyToManyField('subjects_app.Subject', related_name='files', blank=False)
    uploader = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to=pending_upload_path, blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(
        'web_deii_app.User',
        related_name='approved_files',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    approved_at = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='tagged_files', blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name