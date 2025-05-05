from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from .permissions import IsOwnerOrReadOnly


class BaseAllFieldsSerializer(serializers.ModelSerializer):
    """ Базовый сериализатор, использующий все поля модели. """

    class Meta:
        abstract = True
        fields = '__all__'


class AuthorSerializerMixin(serializers.ModelSerializer):
    """Миксин для сериализаторов, содержащих поле 'author'."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )


class BaseViewSet(ModelViewSet):
    """
    Базовый класс для вьюсетов с общими настройками
    разрешений и правил доступа.
    """

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerOrReadOnly()]
