from rest_framework import serializers
from blog.models import Post
from tag.serializers import TagSerializer
from django.db.models import Count

class PostSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    liked_by_user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'poster', 'date', 'tag', 'likes_count', 'liked_by_user']


    def get_likes_count(self, obj):
        return obj.likes.aggregate(Count('id'))['id__count']
    
    def get_liked_by_user(self, obj):
        request = self.context.get('request')
        user = request.user
        if user.is_authenticated:
            return obj.likes.filter(user=user).exists()
        return False