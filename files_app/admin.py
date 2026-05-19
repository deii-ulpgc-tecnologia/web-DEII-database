from django.contrib import admin
from files_app.models import File, Tag


# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass