from rest_framework import generics
from . import models
from . import serializers


class PostListAPI(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
