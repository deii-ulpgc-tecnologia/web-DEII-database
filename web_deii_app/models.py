from django.db import models

class Faq(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    answer = models.TextField()