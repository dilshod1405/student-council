from django.test import TestCase

from post.models import Post
from post.serializers import PostEditSerializer, PostDetailSerializer
from user.models import User


class TestPostEditSerializer(TestCase):
    def setUp(self) -> None:
        self.post = Post.objects.create(title='school', comment='best')

    def test_data(self):
        data = PostEditSerializer(self.post).data
        print(data)
        assert data['title'] == 'school'
        assert data['comment'] == 'best'
