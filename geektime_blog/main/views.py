from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import PostModel, CommentModel
from .forms import PostForm, CommentForm


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def posts(request):
    """帖子列表页"""
    posts = PostModel.objects.order_by('-id')
    context = {
        'posts': posts,
    }
    return render(request, 'main/posts.html', context)


def post(request, post_id):
    """帖子详情页"""
    post = PostModel.objects.get(id=post_id)

    comments = post.commentmodel_set.order_by('-id')

    comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'main/post.html', context)


@login_required()
def add_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.creator = request.user
            new_post.save()
            return redirect('main:posts')

    context = {
        'form': form,
    }

    return render(request, 'main/add_post.html', context)


@login_required()
def edit_post(request, post_id):
    post = PostModel.objects.get(id=post_id)
    if post.creator != request.user:
        raise Http404

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:posts')

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'main/edit_post.html', context)


@login_required()
def delete_post(request, post_id):
    post = PostModel.objects.get(id=post_id)
    if post.creator != request.user:
        raise Http404

    post.delete()
    return redirect('main:posts')


@login_required()
def add_comment(request, post_id):
    post = PostModel.objects.get(id=post_id)

    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.creator = request.user
            new_comment.post = post
            new_comment.save()

    return redirect('main:post', post_id=post_id)


@login_required()
def delete_comment(request, comment_id):
    comment = CommentModel.objects.get(id=comment_id)
    if comment.creator != request.user:
        raise Http404

    comment.delete()
    return redirect('main:post', post_id=comment.post.id)
