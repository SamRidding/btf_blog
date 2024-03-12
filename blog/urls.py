from django.urls import path
from . import views

urlpatterns = [
     path("", views.Blog.as_view(), name="blog"),
     path("search/", views.search, name="search"),
     path('<slug:slug>/', views.BlogPost.as_view(), name='blog_post'),
     path('genre/<slug:tag_slug>/', views.GenreFilter.as_view(), name='filter_genre'),
]