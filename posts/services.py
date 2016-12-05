from .models import Post


class PostService(object):

    def get_all_published(self):

        return Post.objects.all().filter(is_published=True)
