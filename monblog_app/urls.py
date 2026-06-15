from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_articles, name='liste'),
    path('article/<int:pk>/', views.detail_article, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('confirmation/', views.confirmation, name='confirmation'),
]