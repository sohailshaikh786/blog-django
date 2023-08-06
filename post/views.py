from django.shortcuts import render
from .models import Post
# Create your views here.
def home(request):
    send = Post.objects.all()

    return render(request ,'index.html',{'posts': send})

def post(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request,'post.html',{'posts': posts})