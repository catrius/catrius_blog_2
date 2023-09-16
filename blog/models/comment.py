from django.db import models


class Comment(models.Model):
    commenter = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE, related_name = 'comments')

    def __str__(self):
        return self.commenter

    class Meta:
        ordering = ['-created_at']
        get_latest_by = '-created_at'
