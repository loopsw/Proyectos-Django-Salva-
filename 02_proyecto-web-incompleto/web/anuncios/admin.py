from django.contrib import admin
from .models import Anuncio

# Register your models here.
class AnuncioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Anuncio,AnuncioAdmin)
