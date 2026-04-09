import uuid

from django.db import models

class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=255, blank=False, null=False)

class Faq(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, blank=False, null=False)
    question = models.CharField(max_length=255, blank=False, null=False)
    answer = models.TextField(max_length=2048)
