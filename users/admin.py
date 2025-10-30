from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {
            'fields': ('phone', 'date_of_birth', 'bio', 'avatar')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {
            'fields': ('phone', 'date_of_birth', 'bio', 'avatar')
        }),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')