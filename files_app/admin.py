from django.contrib import admin
from files_app.models import File


# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass