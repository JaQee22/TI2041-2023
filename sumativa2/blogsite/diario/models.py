from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    fecha = models.DateTimeField(default=timezone.now)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()

    def __str__(self):
        return self.titulo
 