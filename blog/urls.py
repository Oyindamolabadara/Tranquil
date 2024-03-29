"""Blog posts urls"""
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    AddCommentView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path
    ('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path
    ('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('blogpost-like/<int:pk>', views.LikeView, name="blogpost_like"),
    path
    ('post/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),
]
