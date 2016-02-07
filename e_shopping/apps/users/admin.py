from django.contrib import admin

# Register your models here.

from users.models import (UserProfile, Relationship)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "user_role", "product_count","product_price_limit")

    @staticmethod
    def has_add_permission(request, obj=None):
        return True


# admin.site.register(Parents)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Relationship)

