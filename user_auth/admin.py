from django.contrib import admin
from .models import User, UserFile
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from allauth.account.admin import EmailAddress
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.contrib.auth.forms import UserCreationForm

admin.site.unregister(EmailAddress)
admin.site.unregister(Group)
admin.site.unregister(Site)


def make_access(modeladmin, request, queryset):
    queryset.update(is_access=True)
make_access.short_description = 'Дать доступ в экзамен'

class UserFileAdmin(admin.StackedInline):
    model = UserFile


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    inlines = [UserFileAdmin]
    actions = [make_access]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'email', 'username', 'first_name', 'last_name', 'phone', 'avatar', 'dob', 'password1', 'password2'),
        }),
    )
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone', 'dob', 'date_joined', 'last_login',
                    'is_access']

    fieldsets = (
        (None,
         {'fields': ('username', 'email')}),
        (('Personal info'),
         {'fields': (
             'first_name', 'last_name', 'phone', 'dob', 'avatar')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_access',),
        }),
        ('Дата и время', {'fields': ('last_login', 'date_joined')}),
    )
