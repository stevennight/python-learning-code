from django.forms import ModelForm

from .models import PostModel, CommentModel


class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = ["title", "content"]


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['content']
