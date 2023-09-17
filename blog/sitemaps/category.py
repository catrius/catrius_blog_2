from django.contrib.sitemaps import Sitemap

from blog.models import Category


class CategorySitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
