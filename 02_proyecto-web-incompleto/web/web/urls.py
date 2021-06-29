from django.contrib import admin
from django.urls import path
from anuncios import views
from django.conf import settings
#from django.conf.urls import static

urlpatterns = [
    path('',views.mostrarIndex),
    path('anuncios/',views.mostrarAnuncios,name='anuncios'),
    path('admin/', admin.site.urls),
    path('imagen/',views.mostrarImagen)
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)