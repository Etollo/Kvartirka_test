from django.urls import path

from .views import *

urlpatterns = [
    path('', blog_list, name='blog_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete', PostDelete.as_view(), name='post_delete_url'),
    path('comment/create/', CommentCreate.as_view(), name='comment_create_url'),
    path('comment/<int:object_id>/', CommentDetail.as_view(), name='comment_detail_url'),
    path('comment/<int:object_id>/update', CommentUpdate.as_view(), name='comment_update_url'),
    path('comment/<int:object_id>/delete', CommentDelete.as_view(), name='comment_delete_url')
]