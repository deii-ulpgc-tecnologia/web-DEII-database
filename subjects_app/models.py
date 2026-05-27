from django.db import models

# Create your models here.

class DegreeEnum(models.TextChoices):
    GII = "GII", "Ingeniería Informática"
    GCID = "GCID", "Ciencia e Ingeniería de Datos"
    GIFM = "GIFM", "Ingeniería Física y Matemática"

class YearEnum(models.IntegerChoices):
    YEAR1 = 1, "primero"
    YEAR2 = 2, "segundo"
    YEAR3 = 3, "tercero"
    YEAR4 = 4, "cuarto"
    YEAR5 = 5, "quinto"
    YEAR6 = 6, "sexto"
    MASTER = 7, "master"
    PHD = 8, "phd"

class Subject(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    code = models.CharField(max_length=255, blank=False, null=False)
    degree = models.CharField(max_length=255, choices=DegreeEnum, default=DegreeEnum.GII, blank=False, null=False)
    year = models.IntegerField(choices=YearEnum, default=YearEnum.YEAR1, blank=False, null=False)
    semester = models.IntegerField(blank=False, null=False)
    area = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name