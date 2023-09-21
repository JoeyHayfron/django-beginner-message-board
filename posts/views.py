from django.views.generic import TemplateView, ListView
from .models import Posts

# Create your views here.
class PostsList(ListView):
    model = Posts
    template_name = 'posts.html'
    context_object_name = 'all_posts_list'