from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    View
)

from .models import (
    Post
)

from .services import (
    PostService
)


class ListView(View):

    def get(self, request):
        post_service = PostService()
        posts = post_service.get_all_published()
        context = {
            'posts': posts
        }
        return render(request, 'posts/list.html', context)


class DetailView(View):

    def get(self, request, slug):
        post_service = PostService()
        post = post_service.get_published_or_404(slug)
        context = {
            'post': post
        }
        return render(request, 'posts/detail.html', context)
