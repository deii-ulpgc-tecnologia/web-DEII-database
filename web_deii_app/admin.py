from web_deii_app.models import Faq, User

from django.contrib import admin


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
