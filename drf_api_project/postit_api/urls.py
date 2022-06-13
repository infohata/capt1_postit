from django.urls import path
from . import views


urlpatterns = [
    path('api/posts/', views.PostListCreateAPI.as_view()),
    path('api/posts/<int:pk>/', views.PostDetailUpdateDeleteAPI.as_view()),
]
