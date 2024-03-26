from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import CustomUser

# Unregister the default Group model
admin.site.unregister(Group)

# Custom group admin
class CustomGroupAdmin(admin.ModelAdmin):
    pass

# Register your custom Group model
admin.site.register(Group, CustomGroupAdmin)

# Custom user admin
class CustomUserAdmin(BaseUserAdmin):
    # Specify fields to display in the user list
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

    # Add filters for user list
    list_filter = ('is_staff', 'is_active')

    # Define fieldsets to display in add/edit forms
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Customize the add/edit form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')}
        ),
    )

# Register the custom user model with the customized admin interface
admin.site.register(CustomUser, CustomUserAdmin)
