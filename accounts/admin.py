from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm,CustomUserChangeForm

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
    "email",
    "username",
    "name",
    "is_staff",
    ] 
    # Define fieldsets explicitly instead of inheriting from UserAdmin
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("name", "email", "first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "name", "password1", "password2"),
        }),
    )
admin.site.register(CustomUser, CustomUserAdmin)