from django.contrib import admin
from django.urls import path
from anuncios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home',views.home),
    path('hora',views.hora_actual),
    path('year/<int:year>',views.edad),
]
