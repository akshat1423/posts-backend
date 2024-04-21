from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer

class PostCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(author=self.request.user)

from django.db.models import Q
class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            # if self.request.user.is_staff:  # If user is staff, show all posts
            #     return Post.objects.all()
            # else:
                return Post.objects.filter(is_private=False) | Post.objects.filter(author=self.request.user, is_private=True)
        else:
            return Post.objects.filter(is_private=False)
    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
    # # queryset = Post.objects.all()
    # serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     # Check if the user is authenticated
    #     print(self.request.user.is_authenticated)
    #     if self.request.user.is_authenticated:
    #         # Return posts that are either not private or are private but belong to the user
    #         print(self.request.user.is_authenticated)
    #         # print(Post.objects.get(author=self.request.user))
    #         # print(Post.objects.all())
    #         print(Post.objects.filter(
    #             Q(is_private=False) | Q(author=self.request.user) 
    #         ).first())
    #         return Post.objects.filter(
    #             Q(is_private=False) | Q(author=self.request.user) 
    #         ).first()
    #     else:
    #         print(self.request.user.is_authenticated)
    #         # If the user is not authenticated, only return posts that are not private
    #         return Post.objects.filter(is_private=False)

    # def perform_update(self, serializer):
    #     serializer.save(author=self.request.user)


    #     from django.db import models
# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Post
# from .serializers import PostSerializer
# from django.db.models import Q

# class PostCreateAPIView(APIView):
#     """
#     API view to create a new post.
#     """
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(author=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class PostListCreate(generics.ListCreateAPIView):
#     """
#     API view to list all posts or create a new post. Filters posts so users can only see public posts
#     or their own private posts.
#     """
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
        
#         if self.request.user.is_authenticated:
#             return Post.objects.filter(models.Q(is_private=False) | models.Q(author=self.request.user))
#         return Post.objects.filter(is_private=False)

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
# from django.db.models import Q
# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from .models import Post
# from .serializers import PostSerializer

# class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get_queryset(self):
#         queryset = Post.objects.filter(
#             Q(is_private=False) | Q(author=self.request.user)
#         ) if self.request.user.is_authenticated else Post.objects.filter(is_private=False)
#         print(f"Queryset for user {self.request.user}: {queryset.query}")
#         return queryset



#     def retrieve(self, request, *args, **kwargs):
#         try:
#             instance = self.get_object()
#             serializer = self.get_serializer(instance)
#             return Response(serializer.data)
#         except :
#             return Response({'message': 'Post not found or you do not have permission to view it.'}, status=status.HTTP_404_NOT_FOUND)

#     def perform_update(self, serializer):
#         instance = self.get_object()
#         if instance.author != self.request.user:
#             raise permissions.PermissionDenied("You cannot edit a post you do not own.")
#         serializer.save()

