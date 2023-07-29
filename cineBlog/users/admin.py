from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class AdminUser(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'user_type']
    #fieldsets = campos en ingles
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('profile_pic', 'user_type')}),
    )

admin.site.register(User, AdminUser)