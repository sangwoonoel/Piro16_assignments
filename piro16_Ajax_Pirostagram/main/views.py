from turtle import pos
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'main/post_list.html', ctx)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'main/post_new.html', ctx)

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']

    post = Post.objects.get(id = post_id)
    if post.like == 0:
        post.like = 1
    else:
        post.like = 0
        

    post.save()

    return JsonResponse({'id': post_id, 'like': post.like})

@csrf_exempt
def write_comment(request):
    req = json.loads(request.body)
    id = req['id']
    type = req['type']
    message = req['message']

    post = Post.objects.get(id=id)
    comment = Comment.objects.create(post=post, message=message)
    comment.save()
    return JsonResponse({'id': id, 'type': type, 'message': message, 'comment_id': comment.id})


@csrf_exempt
def del_comment(request):
    req = json.loads(request.body)
    comment_id = req['id']

    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return JsonResponse({'id': comment_id})