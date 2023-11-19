from django.shortcuts import render

from .models import Category, Hashtag, Post

def home_page(request):
    # Obtener todas las categorías

    categories = Category.objects.all().order_by().values()

    # Obtener todos los hashtags

    hashtags = Hashtag.objects.all()

    # Obtener todas las publicaciones

    publications = Post.objects.all().order_by('-fecha'). values()

    context = {
    'categories':categories,'hashtags':hashtags,'publications':publications}

    # Renderizar la plantilla con los datos obtenidos

    return render( request, 'blog_home.html' , context = context)