from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author_id = serializers.ReadOnlyField(source='author.id') 
    is_private = serializers.BooleanField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'summary', 'content', 'image', 'author_name', 'author_id', 'is_private']  # Include 'author_id' and 'is_private'
