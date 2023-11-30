from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('buscar_disponibilidade', views.buscar_disponibilidade, name='buscar_disponibilidade'),
    path('more_info', views.more_info, name='more_info'),
    path('buscar_horario', views.buscar_horario, name='buscar_horario'),
]

