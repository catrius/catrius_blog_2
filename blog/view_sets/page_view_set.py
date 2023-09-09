from rest_framework import serializers, viewsets

from blog.models import Page


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = [
            'title',
            'slug',
            'content',
            'created_at',
            'updated_at',
        ]


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'
