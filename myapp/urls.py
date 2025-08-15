from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),


    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_view'),
    path('article/create', views.ArticleCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update', views.ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:id>/delete', views.delete_article),
    
    path('author/create', views.create_author),
    
    path('home/', views.home),
    path('about/', views.about),
    path('', views.ArticleListView.as_view() , name='article_list')
]
