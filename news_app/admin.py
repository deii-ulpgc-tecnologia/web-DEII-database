from django.contrib import admin

from news_app.models import NewsPost


# Register your models here.
@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    pass