from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name='post_new'),
    path('like_ajax/', views.like_ajax, name = 'like_ajax'),
    path("write_comment/", views.write_comment, name='write_comment'),
    path("del_comment/", views.del_comment, name='del_comment'),
]
