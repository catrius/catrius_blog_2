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
class CommentViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Comment.objects.select_related('post')
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = self.queryset
        post = self.request.query_params.get('post')

        if post is not None:
            queryset = queryset.filter(post__slug = post)
        return queryset
