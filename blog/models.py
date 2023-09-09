from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 300)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(unique = True)
    content = RichTextField()
    thumbnail = models.ImageField(upload_to = 'thumbnails/')
    excerpt = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        get_latest_by = 'created_at'


class Page(models.Model):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(unique = True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        get_latest_by = 'created_at'
