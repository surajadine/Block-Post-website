from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .models import Post


# Create your views here.
# def post_list(request):
#     post_list = Post.objects.all()
#     paginator = Paginator(post_list,1)
#     page_number = request.GET.get('page',1)
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request,'blog/post/list.html',{'posts':posts})

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    
    

def post_details(request,year,month,day,slug):
    post = get_object_or_404(Post,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day,
                             slug = slug)
    return render(request,'blog/post/detail.html',{'post':post})

