from blog.sitemaps.category import CategorySitemap
from blog.sitemaps.page import PageSitemap
from blog.sitemaps.post import PostSitemap

sitemaps = {
    'posts': PostSitemap,
    'categories': CategorySitemap,
    'pages': PageSitemap,
}
