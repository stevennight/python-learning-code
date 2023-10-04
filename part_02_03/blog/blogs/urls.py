from django.urls import path, include

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name="index"),
    path('add_post/', views.add_post, name="add_post"),
    path('edit_post/<int:post_id>', views.edit_post, name="edit_post"),
]