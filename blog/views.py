# blog/views.py
from django.views.generic import ListView, DetailView
from . models import Post

# Create your views here.
class BlogListView(ListView): # pylint: disable=too-many-ancestors
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
