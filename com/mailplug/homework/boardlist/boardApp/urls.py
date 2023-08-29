from django.urls import path
from . import views

urlpatterns = [
    path('boards/', views.DRFBoardListView.as_view(), name='drf-board-list'),
    path('boards/<int:pk>/', views.DRFBoardDetailView.as_view(), name='drf-board-detail'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]
