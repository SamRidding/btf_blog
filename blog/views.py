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
        queryset = Post.objects.filter(mix=False)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "blog/blog_post.html",
            {
                "post": post,
            },
        )


class GenreFilter(generic.ListView):
    """View to filter blog posts by genre tag"""

    model = Post
    template_name = "blog/blog.html"

    def get_queryset(self):

        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug'))
    

def search(request):
    """View to search blog posts"""

    if request.method == "POST":
        searched = request.POST.get('searched')
        results = Post.objects.filter(title__icontains=searched)
        return render(request, 'blog/search.html',
                      {'searched': searched,
                       'results': results, })
    else:
        return render(request, 'blog/search.html')
