
from django.contrib import admin
from django.urls import path

from platzigram import views as localViews
from posts import views as postsViews

urlpatterns = [
    path('admin', admin.site.urls),
    path('hello/', localViews.holaMundo),
    path('hola',localViews.sort_integers),
    path('hi/<str:nombre>/<int:edad>', localViews.say_hi),
    path('posts/',postsViews.postList),
]
