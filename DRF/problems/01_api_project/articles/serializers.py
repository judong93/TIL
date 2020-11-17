from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'content', 'article',)
        read_only_fields = ('article',)


class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title',)


class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(
        many=True,
        # 리드 온리필드로 쓸 건데, 만약 내가 필드를 추가하거나
        # 재정의 한거라면 넣어줘야 함.
        read_only=True 
    )
    comment_count = serializers.IntegerField(
        source='comment_set.count',
        read_only=True
    )

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ['id', 'title', 'content', 'comment_set', 'comment_count',]
        read_only_fields = ['comment_set', 'comment_count',]

