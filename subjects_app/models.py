from django.db import models

# Create your models here.
class YearEnum(models.IntegerChoices):
    YEAR1 = 1, "primero"
    YEAR2 = 2, "segundo"
    YEAR3 = 3, "tercero"
    YEAR4 = 4, "cuarto"
    YEAR5 = 5, "quinto"
    YEAR6 = 6, "sexto"
    MASTER = 7, "master"
    PHD = 8, "phd"


class SemesterEnum(models.IntegerChoices):
    FIRST = 1
    SECOND = 2
    YEAR_LONG = 3, "anual"


class Degree(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    abbreviation = models.CharField(max_length=255, blank=False, null=False)


class knowledge_area(models.Model):
    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=255, blank=False, null=False)


class Subject(models.Model):
    id = models.IntegerField(blank=False, null=False, primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    abbreviation = models.CharField(max_length=255, blank=False, null=False)
    degree = models.ForeignKey(Degree, on_delete=models.PROTECT, blank=False, null=False)
    year = models.IntegerField(choices=YearEnum, default=YearEnum.YEAR1, blank=False, null=False)
    semester = models.IntegerField(choices=SemesterEnum, default=SemesterEnum.FIRST, blank=False, null=False)
    area = models.ManyToManyField(knowledge_area, blank=False)

    def __str__(self):
        return self.name


class MyModel(models.Model):
    pass