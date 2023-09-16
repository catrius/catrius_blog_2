from rest_framework import serializers, viewsets

from blog.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
        ]
        lookup_field = 'slug'


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
