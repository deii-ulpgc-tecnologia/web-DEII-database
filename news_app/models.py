from django.db import models

# Create your models here.
class NewsPost(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('web_deii_app.User', related_name='posts_id', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    publish_date = models.DateField(blank=False, null=False)
    edited_date = models.DateField(null=True)

    def __str__(self):
        return self.title