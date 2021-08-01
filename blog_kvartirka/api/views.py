from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin

from ..models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class ListPostView(RetrieveModelMixin, CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SinglePostView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListCommentView(CreateModelMixin, ListModelMixin, GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SingleCommentView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
