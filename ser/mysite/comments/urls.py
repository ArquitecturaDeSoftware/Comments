from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import comment
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^post/$', comment.post_list),
    url(r'^posts/(?P<restaurant_id>.+)$', comment.PostList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
