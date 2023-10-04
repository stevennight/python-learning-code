from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('post/<int:post_id>', views.post, name='post'),
    path('add_comment/<int:post_id>', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
]