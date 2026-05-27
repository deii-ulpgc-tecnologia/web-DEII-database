from django.db import models

# Create your models here.

class DegreeEnum(models.TextChoices):
    gii = "GII", "Ingeniería Informática"
    gcid = "GCID", "Ciencia e Ingeniería de Datos"
    gifm = "GIFM", "Ingeniería Física y Matemática"

class Subject(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    code = models.CharField(max_length=255, blank=False, null=False)
    degree = models.CharField(max_length=255, choices=DegreeEnum, default=DegreeEnum.gii, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    semester = models.IntegerField(blank=False, null=False)
    area = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name