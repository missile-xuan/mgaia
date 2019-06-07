from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
# Create your views here.


def post_list(request): # 获取已经发布的帖子

    object_list = Post.published.all()
    paginator = Paginator(object_list,3)    #每页三篇
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #如果页不是整数，则传递第一页
        posts = paginator.page(1)
    except EmptyPage:
        # 如果页面超出范围，则传递最后一页结果
        posts = paginator.page(paginator.num_pages)


    return render(request, 'blog/post/list.html', {'page':page,'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)

    return render(request,'blog/post/datail.html',{'post':post})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
