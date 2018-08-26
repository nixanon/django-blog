# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Post


# Create your views here.
class BlogListView(ListView): # pylint: disable=too-many-ancestors
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView): # pylint: disable=too-many-ancestors
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): # pylint: disable=too-many-ancestors
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView): # pylint: disable=too-many-ancestors
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'

class BlogDeleteView(DeleteView): # pylint: disable=too-many-ancestors
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
