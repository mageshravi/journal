from django.test import (
    TestCase,
    Client
)
from .models import (
    Post
)
from .services import (
    PostService
)


class PostServiceTest(TestCase):

    def setUp(self):
        Post.objects.create(
            title="First Post",
            content="Hello world content for first post",
            url="http://alpha.journal.com/first-post/",
            is_published=True
        )
        Post.objects.create(
            title="Draft Post",
            content="Sample content for draft post",
            url="http://alpha.journal.com/draft-post/",
            is_published=False
        )

    def test_published_posts(self):
        post_service = PostService()
        posts = post_service.get_all_published()
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0].title, "First Post")
