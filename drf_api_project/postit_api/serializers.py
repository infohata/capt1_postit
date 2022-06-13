from rest_framework import serializers
from . import models


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = models.Comment
        fields = ('id', 'user', 'user_id', 'post', 'body', 'created', )


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comments = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Post
        fields = (
            'id', 'user', 'user_id', 'title', 'body', 'created', 
            'comments', 'comment_count', 
        )

    def get_comment_count(self, obj):
        return obj.comments.count()
