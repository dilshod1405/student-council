from django.contrib import admin

from post.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_created', 'author', 'file', 'id')
    ordering = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    ordering = ['id']
