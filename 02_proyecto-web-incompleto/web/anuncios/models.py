from django.db import models
from django.utils import timezone

class Anuncio(models.Model):
    STATUS_CHOICES = (
        ('borrador','Borrador'),
        ('publicado','Publicado'),
    )

    title = models.CharField(max_length=150,verbose_name="Título")
    content = models.TextField(verbose_name="Contenido",help_text="Enter field documentation")
    author = models.CharField(max_length=150,null=False,default='undefined',verbose_name="Autor de la publicacion")
    image = models.ImageField(null=True,upload_to='images',verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    #updated = models.DateTimeField(editable=True,default=timezone.now,verbose_name="Última actualización")
    updated = models.DateTimeField(auto_now=True,verbose_name="Última actualización")

    state = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='borrador',
                                verbose_name="Estado",
                            )
class Meta:
    #abstract = True
    verbose_name="Noticia"
    verbose_name_plural='Noticias'
    ordering = ('-created',)
def __str__(self):
    return self.title
    
