import uuid

from django.db import models


# TODO users

class Subjects(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    degree = models.CharField(max_length=255, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    semester = models.IntegerField(blank=False, null=False)
    area = models.CharField(max_length=255, blank=False, null=False)


def file_path(instance, filename):
    return "{0}/{1}".format(instance.subject_id, filename) # id_de_asignatura/archivo


class Files(models.Model):
    id = models.AutoField(primary_key=True)
    subject_id = models.ManyToManyField(Subjects, related_name='files_id', blank=False)
    uploader = models.CharField(max_length=255, blank=False, null=False)
    file = models.FileField(upload_to=file_path, blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=False)
    # TODO approver_id
    publish_date = models.DateField(blank=False, null=False)


class NewsPosts(models.Model):
    id = models.AutoField(primary_key=True)
    # todo user_id
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    is_active = models.BooleanField(default=False)
    pinned = models.BooleanField(default=False)
    publish_date = models.DateField(blank=False, null=False)
    edited_date = models.DateField(blank=False, null=False)


class Faq(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, blank=False, null=False)
    question = models.CharField(max_length=255, blank=False, null=False)
    answer = models.TextField(max_length=2048)
