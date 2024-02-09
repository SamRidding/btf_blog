from django.shortcuts import render
from django.views import generic, View

from .models import Post

class Blog(generic.ListView):
    """View to display posts on blog page"""

    model = Post
    template_name = "blog/blog.html"
