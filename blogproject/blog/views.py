from django.shortcuts import render
from .models import post
# Create your views here.
def pub_post_list(request):
    posts = post.objects.all()
    c = {
        'post_list' : posts ,
    }
    return render(request , "post_list.html" , context=c )

def pub_post_list(request):
    posts = post.objects.filter(states = 1)
    c = {
        'post_list' : posts ,
    }
    return render(request , "post_list.html" , context=c )

def unpub_post_list(request):
    posts = post.objects.filter(states = 0)
    c = {
        'post_list' : posts ,
    }
    return render(request , "post_list.html" , context=c )
