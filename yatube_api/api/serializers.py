from django.contrib.auth import get_user_model
from rest_framework import serializers

from .mixins import BaseAllFieldsSerializer, AuthorSerializerMixin
from posts.models import Comment, Post, Group, Follow


User = get_user_model()


class PostSerializer(BaseAllFieldsSerializer, AuthorSerializerMixin):
    """Сериализатор для работы с постами."""

    class Meta(BaseAllFieldsSerializer.Meta):
        model = Post


class GroupSerializer(BaseAllFieldsSerializer):
    """Сериализатор для работы с группами."""

    class Meta(BaseAllFieldsSerializer.Meta):
        model = Group


class CommentSerializer(BaseAllFieldsSerializer, AuthorSerializerMixin):
    """Сериализатор для работы с комментариями."""

    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta(BaseAllFieldsSerializer.Meta):
        model = Comment


class FollowSerializer(BaseAllFieldsSerializer):
    """Сериализатор для работы с подписками."""

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta(BaseAllFieldsSerializer.Meta):
        model = Follow

    def validate(self, attrs):
        if 'following' not in attrs:
            raise serializers.ValidationError(
                {'following': 'Поле "following" обязательно.'}
            )

        current_user = self.context['request'].user

        if attrs['following'].id == current_user.id:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.'
            )
        return attrs
