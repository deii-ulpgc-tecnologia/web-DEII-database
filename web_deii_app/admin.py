from web_deii_app.models import Faq

from django.contrib import admin


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    pass
