from django.test import TestCase, SimpleTestCase
from .models import Posts
from django.urls import reverse

# Create your tests here.
class PostsModelTest(TestCase):
    def setUp(self):
        Posts.objects.create(text="just a test")
        
    def test_text_content(self):
        post = Posts.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')
    
class HomePageViewTest(TestCase):
    def setUp(self):
        Posts.objects.create(text="another one")
        
    def test_view_url_exists_at_proper_locations(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'posts.html')
    
