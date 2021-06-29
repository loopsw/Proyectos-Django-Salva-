from django.contrib import admin
from django.urls import path,include
from anuncios.views import anuncios,index
from empresa.views import mostrarEmpresa


urlpatterns = [
    path('',index,name="inicio"),
    path('empresa/',mostrarEmpresa,name="empresa"),
    path('admin/', admin.site.urls),
    path('anuncios/',anuncios, name="anuncios"),
    path('',include('sendemail.urls')),
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('redirect/', RedirectView.as_view(url='/anuncios/', permanent=True)),
]


from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

