from django.contrib import admin
from .models import Hafez_Fall, UserInformation


class AdminUserInformation(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'first_name', 'last_name')


class AdminHafezFall(admin.ModelAdmin):
    list_display = ('id', 'text', 'description')
    ordering = ('id',)


admin.site.register(Hafez_Fall, AdminHafezFall)
admin.site.register(UserInformation, AdminUserInformation)
