from rest_framework import viewsets, pagination, generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic import ListView, DetailView
from .models import Board, Post
from .serializers import BoardSerializer, PostSerializer

# 게시판 목록과 생성을 위한 DRF 뷰
class DRFBoardListView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

# 단일 게시판의 조회, 업데이트, 삭제를 위한 DRF 뷰
class DRFBoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer  # 게시판 내의 게시물을 포함하기 위한 중첩 Serializer

# 게시물에 대한 페이지네이션 설정
class PostPagination(pagination.PageNumberPagination):
    page_size = 10

# 게시물의 목록, 생성, 업데이트, 삭제를 위한 DRF 뷰
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']  # PostViewSet에 대한 필터 옵션

# 단일 게시물 조회를 위한 DRF 뷰
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 게시판 목록을 위한 뷰
class BoardListView(ListView):
    model = Board
    template_name = 'board_list.html'

# 단일 게시판을 표시하기 위한 뷰
class BoardDetailView(DetailView):
    model = Board
    template_name = 'board_detail.html'