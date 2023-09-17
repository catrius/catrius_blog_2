from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 300)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category/{self.slug}/'

    @property
    def updated_at(self):
        return self.posts.first().updated_at

    class Meta:
        verbose_name_plural = 'categories'
