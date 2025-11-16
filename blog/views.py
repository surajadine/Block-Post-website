from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request,'blog/post/list.html',{'posts':posts})

def post_details(request,post_slug):
    post = get_object_or_404(Post,slug=post_slug)
    return render(request,'blog/post/detail.html',{'post':post})

