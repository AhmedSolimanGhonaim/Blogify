from rest_framework import generics 
from .permissions import IsAuthorOrReadOnly
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer,UserSerializer
from django.contrib.auth import get_user_model

# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthorOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset=get_user_model().objects.all()
    serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer





class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer