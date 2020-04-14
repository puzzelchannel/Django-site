from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/favourite_post', views.favourite_post, name='favourite_post'),
    path('favourite/', views.post_favourite_list, name='post_favourite_list'),
]
