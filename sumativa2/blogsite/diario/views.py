from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    publicaciones = Post.objects.all().order_by('-fecha').values()
    context = {'publicaciones': publicaciones}
    return render(request, 'index.html', context)