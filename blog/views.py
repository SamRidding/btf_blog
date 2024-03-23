from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.base import TemplateView

from .models import Post

class Blog(generic.ListView):
    """View to display posts on blog page"""

    model = Post
    template_name = "blog/blog.html"
    context_object_name = "posts"
    paginate_by = 8
    ordering = ['-posted_on']

    def get_template_names(self, *args, **kwargs):
        if self.request.htmx:
            return "blog/post_list.html"
        else:
            return self.template_name



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
    

class Mixes(TemplateView):
    """View to display mixes page"""

    template_name = "blog/mixes.html"


class GenreFilter(generic.ListView):
    """View to filter blog posts by genre tag"""

    model = Post
    template_name = "blog/genre_filter.html"
    context_object_name = 'genres'

    def get_queryset(self):
        print(self.kwargs)
        print(Post.objects.filter(tags__slug=self.kwargs.get('tag_slug')))
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
