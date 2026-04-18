from web_deii_app.models import Faq, File, NewsPost, Subject, User

from django.contrib import admin


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    pass


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass