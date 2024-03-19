from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):

    list_display = ('username', 'email_id', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser')

    list_display_links = ('username', 'email_id')

    readonly_fields = ('is_admin', 'is_active', 'is_staff', 'is_superuser', 'date_joined', 'last_login')

    ordering = ('-last_login',)

    filter_horizontal = ()

    list_filter = ()

    fieldsets = ()


admin.site.register(Account, AccountAdmin)