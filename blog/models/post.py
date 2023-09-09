from ckeditor.fields import RichTextField
from django.db import models

from blog.models import Category


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
