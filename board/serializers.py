from rest_framework import serializers
from .models import Board, Comments

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.nickname')
    post = serializers.ReadOnlyField(source='post.id')
    post = serializers.CharField(read_only=True)
    
    class Meta:
        model = Comments
        fields = ['id', 'post', 'user', 'created_at', 'comment']

class BlogSerializer(serializers.ModelSerializer):
    
    user = serializers.CharField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'user', 'title', 'body', 'comments']


