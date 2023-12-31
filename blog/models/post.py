from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length = 300)
    slug = models.SlugField(unique = True)
    content = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to = 'thumbnails/')
    excerpt = models.TextField(blank = True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE, related_name = 'posts')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    highlight = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/post/{self.slug}/'

    @property
    def comment_count(self):
        return self.comments.count()

    class Meta:
        ordering = ['-created_at']
        get_latest_by = '-created_at'
