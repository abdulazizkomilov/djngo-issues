from django.shortcuts import render
from .models import Post
# Create your views here.
class PagesListView(ListView):
    model = Post
    temlate_name = 'ome.html'

class PagesDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'