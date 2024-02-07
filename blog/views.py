from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk')
    content = {'posts' : posts,
               }
    return render(request, 'blog/index.html', content)

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    content = {'post' : post}
    return render(request, 'blog/single_post_page.html', content)