from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

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
