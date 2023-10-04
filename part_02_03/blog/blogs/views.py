from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    blog_posts = BlogPost.objects.order_by('-date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/index.html', context)

@login_required()
def add_post(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('blogs:index')

    context = {
        'form': form
    }
    return render(request, 'blogs/add_post.html', context)

@login_required()
def edit_post(request, post_id):
    blog_post = BlogPost.objects.get(id=post_id)

    if blog_post.author != request.user:
        raise Http404

    if request.method != 'POST':
        form = BlogPostForm(instance=blog_post)
    else:
        form = BlogPostForm(instance=blog_post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {
        'blog_post': blog_post,
        'form': form
    }
    return render(request, 'blogs/edit_post.html', context)
