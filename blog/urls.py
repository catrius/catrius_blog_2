from django.contrib.sitemaps.views import sitemap
from django.urls import path
from rest_framework import routers

from blog.sitemaps import sitemaps
from blog.view_sets.category_view_set import CategoryViewSet
from blog.view_sets.comment_view_set import CommentViewSet
from blog.view_sets.page_view_set import PageViewSet
from blog.view_sets.post_view_set import PostViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'pages', PageViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path(
        'sitemap.xml',
        sitemap,
        {"sitemaps": sitemaps},
        name = "django.contrib.sitemaps.views.sitemap",
    )
]
