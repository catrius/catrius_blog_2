from rest_framework import routers

from blog.view_sets.category_view_set import CategoryViewSet
from blog.view_sets.page_view_set import PageViewSet
from blog.view_sets.post_view_set import PostViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'pages', PageViewSet)
router.register(r'categories', CategoryViewSet)
