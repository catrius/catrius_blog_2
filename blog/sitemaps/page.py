from django.contrib.sitemaps import Sitemap

from blog.models import Page


class PageSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.7
    protocol = 'https'

    def items(self):
        return Page.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
