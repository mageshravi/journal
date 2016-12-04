from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .models import (
    Post
)


class ListView(View):

    def get(self, request):
        posts = Post.objects.all().filter(is_published=True)
        context = {
            'posts': posts
        }
        return render(request, 'posts/list.html', context)
