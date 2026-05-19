from django.db import models

# Create your models here.
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    degree = models.CharField(max_length=255, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    semester = models.IntegerField(blank=False, null=False)
    area = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name