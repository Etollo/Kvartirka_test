from django.shortcuts import render, get_object_or_404
from django.views import View

from blog_kvartirka.forms import PostForm, CommentForm
from blog_kvartirka.models import Post, Comment
from blog_kvartirka.utils import ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin, ObjectDetailMixin


def blog_list(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'blog_kvartirka/index.html', context={'posts': posts, 'comments': comments})


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog_kvartirka/post_create_form.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog_kvartirka/post_update_form.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog_kvartirka/post_delete_form.html'
    redirect_url = 'posts_list_url'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog_kvartirka/post_detail.html'


class CommentCreate(ObjectCreateMixin, View):
    model_form = CommentForm
    template = ''


class CommentUpdate(ObjectUpdateMixin, View):
    model = Comment
    model_form = CommentForm
    template = ''


class CommentDelete(ObjectDeleteMixin, View):
    model = Comment
    template = ''
    redirect_url = ''


class CommentDetail(ObjectDetailMixin, View):
    model = Comment
    template = ''
