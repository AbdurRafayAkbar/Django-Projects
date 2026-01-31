from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
def Post_list(request):
    post = Post.objects.all()
    paginator=Paginator(post,2)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    return render(request,"post.html",{"page_obj":page_obj})
