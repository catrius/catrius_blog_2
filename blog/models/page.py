from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Page(models.Model):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(unique = True)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        get_latest_by = 'title'
