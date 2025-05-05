from rest_framework import filters, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from rest_framework.status import HTTP_405_METHOD_NOT_ALLOWED

from posts.models import Post, Group, Comment, Follow
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


class GroupViewSet(ModelViewSet):
    """Представление для работы с группами."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Запрещаем создание группы через API."""
        return Response(
            {"detail": "Создание групп доступно только через админку."},
            status=HTTP_405_METHOD_NOT_ALLOWED
        )


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

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        already_exists = Follow.objects.filter(
            user=self.request.user,
            following=serializer.validated_data['following']
        ).exists()

        if already_exists:
            raise serializers.ValidationError(
                {"message": "Уже подписаны на этого пользователя"},
                code=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().create(request, *args, **kwargs)
        else:
            return Response(
                {"detail": "Требуется авторизация"},
                status=status.HTTP_401_UNAUTHORIZED
            )
