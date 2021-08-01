from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^post/$', views.ListPostView.as_view(), name='list_post'),
    url(r'^post/(?P<pk>\d+)/$', views.SinglePostView.as_view(), name='single_post'),
    url(r'^comment/$', views.ListCommentView.as_view(), name='comment_list'),
    url(r'^comment/(?P<pk>\d+)/$', views.SingleCommentView.as_view(), name='comment_detail'),
]