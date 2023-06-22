from rest_framework import serializers

from post.models import Post, Category
from user.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


# Post Category
class PostCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)


# Post Card
class PostCardSerializer(serializers.ModelSerializer):
    category = PostCategory(read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'is_created', 'file', 'category', 'author')


# Edit Post (create, delete, put, patch)
class PostEditSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(read_only=True)
    # category = PostCategory(read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'file', 'category', 'comment', 'id')


class PostDetailSerializer(serializers.ModelSerializer):
    category = PostCategory(read_only=True)
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'file', 'is_created', 'category', 'author', 'comment')
