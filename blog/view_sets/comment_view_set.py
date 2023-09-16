from rest_framework import serializers, mixins, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from blog.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'commenter',
            'content',
            'updated_at',
        ]


@permission_classes([AllowAny])
class CommentViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
