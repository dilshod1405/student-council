from django.contrib import admin

from user.models import User, Region, District


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'region', 'district', 'phone', 'id')
    ordering = ('id',)
    list_filter = ('first_name', 'last_name', 'region', 'district',)
    list_editable = ['first_name', 'last_name', 'region', 'district', 'phone']
    list_per_page = 100
    search_fields = ['username', 'first_name', 'last_name', 'phone']


@admin.register(Region)
class UserAdmin(admin.ModelAdmin):
    list_display = ('region', 'id')
    ordering = ['id']


@admin.register(District)
class UserAdmin(admin.ModelAdmin):
    list_display = ('district', 'id')
    ordering = ['id']
