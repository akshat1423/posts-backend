from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_private')
    list_filter = ('is_private', 'author')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
