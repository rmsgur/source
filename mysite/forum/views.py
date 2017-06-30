from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Post
from .forms import PostForm, ReplyForm


def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})


@login_required
def create(request):
    params = request.POST if request.method == 'POST' else None
    form = PostForm(params)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        messages.info(request, '帖子《{}》创建成功'.format(post.title))
        form = PostForm()

    return render(request, 'create.html', {'form': form})


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post.html', {'post': post,
                                         'reply_form': ReplyForm()})


@login_required
@require_POST
def reply(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.author = request.user
        reply.post = post
        print(reply.save())
        messages.info(request, '帖子《{}》回复成功'.format(post.title))
    else:
        print('not valid')
        messages.warning(request, '帖子《{}》回复失败')

    return redirect('post', post.id)
