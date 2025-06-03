from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model

from .models import Post


class BlogTest(TestCase):


    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword"
        )
        cls.post = Post.objects.create(
            auth=cls.user,
            title="Test Post",
            body="This is a test post."
        )
    
    def test_post_content(self):
        self.assertEqual(self.post.auth.username, "testuser")
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.body, "This is a test post.")
    


    