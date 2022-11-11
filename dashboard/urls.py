from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('translate', views.translate, name='translate'),
    path('post', views.post, name='post'),
    path('get', views.get, name='get'),
]