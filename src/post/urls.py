from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('posts/create/', views.create_posts, name="create_post"),
    path('posts/<str:id>/', views.view_post, name="view_post"),
]
