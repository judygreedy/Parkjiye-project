from django.db import models

# 게시판 모델
class Board(models.Model):
    id = models.AutoField(primary_key=True)  # 자동으로 증가하는 ID
    name = models.CharField(max_length=100, verbose_name='게시판 이름')  # 게시판 이름
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 시간')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정 시간')

# 게시글 모델
class Post(models.Model):
    id = models.AutoField(primary_key=True)  # 자동으로 증가하는 ID
    board = models.ForeignKey(Board, related_name='posts', on_delete=models.CASCADE, verbose_name='게시판')
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    author_id = models.CharField(max_length=100, verbose_name='작성자 ID')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성 시간')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정 시간')
