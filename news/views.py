from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .filters import PostFilter
from .models import Post, Category


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 5


class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class SoloPost(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_category'] = Post.objects.all().values('post_category__category_title')
        return context
