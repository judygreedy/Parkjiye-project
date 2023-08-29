from rest_framework import serializers
from .models import Board, Post

# 게시판 시리얼라이저
class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
            #['id', 'name', 'posts']

# 게시글 시리얼라이저
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



