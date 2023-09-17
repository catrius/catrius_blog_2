from django.contrib.sitemaps import Sitemap

from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
