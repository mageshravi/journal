from django.shortcuts import get_object_or_404
from .models import Post


class PostService(object):

    def get_all_published(self):

        return Post.objects.all().filter(
            is_published=True
        ).order_by('-published_on')

    def get_published_or_404(self, url):

        return get_object_or_404(Post, url=url, is_published=True)
