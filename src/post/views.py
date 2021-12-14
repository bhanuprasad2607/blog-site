from django.shortcuts import render
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.all().order_by('-post_updated')
    context = {
        'posts': posts,
    }
    return render(request, 'post/home.html', context)


def create_posts(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form,
    }
    return render(request, 'post/post-form.html', context)


def posts(request):
    posts = Post.objects.all().order_by('-post_updated')
    context = {
        'posts': posts
    }
    return render(request, 'post/list-posts.html', context)


def view_post(request, id):
    post = Post.objects.filter(post_id=id).get()
    context = {
        'post': post,
    }
    return render(request, 'post/view-post.html', context)
