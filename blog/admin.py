from django.contrib import admin
from django.db import models
from django.forms import TextInput

from blog.models import Category, Post, Page


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = [
        'name'
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs = {'size': '100'})},
    }
    prepopulated_fields = {'slug': ['title']}

    list_display = [
        'title',
        'excerpt',
        'category',
        'created_at',
        'updated_at',
    ]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs = {'size': '100'})},
    }
    prepopulated_fields = {'slug': ['title']}

    list_display = [
        'title',
        'created_at',
        'updated_at',
    ]
