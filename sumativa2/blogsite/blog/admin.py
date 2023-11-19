from django.contrib import admin
from .models import Category, Hashtag, Post

# Register your models here.

admin.site.register(Category)

admin.site.register(Hashtag)

admin.site.register(Post)