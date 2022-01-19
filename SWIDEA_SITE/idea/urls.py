from django.urls import path
from . import views

app_name='idea'

urlpatterns = [
    path('', views.idea_list, name="idea_list"),
    path('plus_interest/', views.plus_interest, name="plus_interest"),
    path('minus_interest/', views.minus_interest, name="minus_interest"),
    path('<int:pk>/', views.idea_detail, name="idea_detail"),
    path('create/', views.idea_create, name='idea_create'),
    path('<int:pk>/idea_edit/', views.idea_edit, name='idea_edit'),
    path('<int:pk>/idea_delete/', views.idea_delete, name='idea_delete'),
    path('dev/', views.dev_list, name="dev_list"),
    path('<int:pk>/dev/', views.dev_detail, name="dev_detail"),
    path('dev_create/', views.dev_create, name='dev_create'),
    path('<int:pk>/dev_edit/', views.dev_edit, name='dev_edit'),
    path('<int:pk>/dev_delete/', views.dev_delete, name='dev_delete'),
  

    
]