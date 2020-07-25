from django.contrib import admin
from .models import User, UserFile
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


class UserFileAdmin(admin.StackedInline):
    model = UserFile

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    inlines = [UserFileAdmin]
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone', 'dob', 'date_joined', 'last_login']

    fieldsets = (
        (None,
         {'fields': ('username', 'email')}),
        (('Personal info'),
         {'fields': (
             'first_name', 'last_name', 'phone', 'dob',  'avatar')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', ),
        }),
        ('Дата и время', {'fields': ('last_login', 'date_joined')}),
    )
