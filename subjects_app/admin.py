from django.contrib import admin

from subjects_app.models import Subject


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass