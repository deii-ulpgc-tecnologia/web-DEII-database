import os
import uuid
from django.db import models
from django.conf import settings


# Create your models here.
def news_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('news', str(instance.post.id), filename)


class NewsPost(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts_id', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    publish_date = models.DateField(blank=False, null=False)
    edited_date = models.DateField(null=True)
    cover_image = models.ForeignKey(
        'NewsImage',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='cover_of_news_post'
    )

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=news_image_path, blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} - {self.id}"
