from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Post

class Blog(generic.ListView):
    """View to display posts on blog page"""

    model = Post
    template_name = "blog/blog.html"


class BlogPost(View):
    """
    View for individual blog posts, returning all post model
    data
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(draft=False)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/blog_post.html",
            {
                "post": post,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(draft=False)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/blog_post.html",
            {
                "post": post,
            },
        )