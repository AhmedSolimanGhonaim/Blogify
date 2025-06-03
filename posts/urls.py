from .views import PostList , PostDetail
from django.urls import path

urlpatterns = [
    path("posts/", PostList.as_view(), name="post_list"),
    path("posts/<int:pk>", PostDetail.as_view(), name="post_detail"),
]
