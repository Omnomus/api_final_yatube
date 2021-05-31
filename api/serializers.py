from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username', default=CurrentUserDefault())
    following = serializers.SlugRelatedField(
        read_only=False, slug_field='username', queryset=User.objects.all())

    def validate(self, attrs):
        following = User.objects.get(username=attrs['following'])
        if self.context['request'].user == following:
            raise ValidationError('Вы не можете подписаться на самого себя')
        return attrs

    class Meta:
        fields = ('id', 'user', 'following',)
        model = Follow
        validators = [UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=('user', 'following'),
            message='Подписка уже есть'
        )]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pk', 'title',)
        model = Group
