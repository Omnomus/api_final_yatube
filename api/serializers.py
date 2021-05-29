from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    following = serializers.SlugRelatedField(
        read_only=False, slug_field='username', queryset=User.objects.all())

    def validate(self, attrs):
        user = self.context['request'].user
        following = User.objects.get(username=attrs['following'])
        if user == following:
            raise ValidationError(message='Подписка на себя невозможна')

    class Meta:
        fields = ('user', 'following',)
        model = Follow


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pk', 'title',)
        model = Group
