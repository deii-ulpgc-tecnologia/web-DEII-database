from django.contrib import admin
from news_app.models import NewsPost, NewsImage


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 3
    max_num = 10


# Register your models here.
@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'is_active', 'pinned')
    inlines = [NewsImageInline]
