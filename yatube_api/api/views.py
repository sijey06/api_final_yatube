from rest_framework import filters
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from posts.models import Post, Group, Comment
from .mixins import BaseViewSet
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)


class PostViewSet(BaseViewSet):
    """Представление для работы с постами."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """Представление для работы с группами."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class CommentViewSet(BaseViewSet):
    """Представление для работы с комментариями."""

    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(ModelViewSet):
    """Представление для работы с подписками."""

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticated,)
    search_fields = ('user__username', 'following__username')
    http_method_names = ['get', 'post']

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
