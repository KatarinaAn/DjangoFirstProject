from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Posts
from .forms import PostForm
from django.contrib.auth.decorators import login_required  


@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request, 'post_form.html', {'form': form})


def home(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


@login_required
def edit_post(request, id):
    post = get_object_or_404(Posts, id=id)
    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id':id}
        return render(request, 'post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('home')
        else:
            messages.error(request, "")
            return render(request, 'post_form.html', {'form': form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Posts, id=id)
    context = {'id':id}
    if request.method == 'GET':
        return render(request, 'post_delete.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        post.delete()
        messages.success(request, 'Post deleted successfully')
        return redirect('home')