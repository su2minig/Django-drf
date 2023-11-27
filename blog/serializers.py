
from .models import Post
from rest_framework import serializers
from django.contrib.auth import get_user_model


# class AuthorSerializer(ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['email']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    # author = AuthorSerializer()
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['author']