from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username') 

    class Meta:
        model = Post
        fields = ['id', 'title', 'summary', 'content', 'image', 'author_name']  
