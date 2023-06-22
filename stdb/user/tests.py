from django.test import TestCase

from user.models import User
from user.serializers import UserDetailSerializer


class TestUserDetailSerializer(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='tester001', about='Test')

    def test_data(self):
        data = UserDetailSerializer(self.user).data
        print(data)
        assert data['username'] == 'tester001'
        assert data['about'] == 'Test'
