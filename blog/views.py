from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     content = {'posts' : posts,
#                }
#     return render(request, 'blog/index.html', content)

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    content = {'post' : post}
    return render(request, 'blog/single_post_page.html', content)