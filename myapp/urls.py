from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
    path('article/<int:id>/<slug:slug>', views.show_article),
    path('home/', views.home),
    path('about/', views.about),
]
