from rest_framework.serializers import ModelSerializer
from .models import Post
from django.contrib.auth import get_user_model


# class AuthorSerializer(ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['email']


class PostSerializer(ModelSerializer):
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