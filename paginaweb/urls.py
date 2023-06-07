from django.urls import path 
from . import views

urlpatterns =[
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('crearcuenta', views.crearcuenta, name='crearcuenta'),
    path('iniciosession', views.iniciosession, name='iniciosession'),
    path('rw', views.rw, name='rw'),
    path('perro', views.perro, name='perro'),
    path('perro2', views.perro2, name='perro2'),
    path('artistas', views.artistas, name='artistas'),
    path('esculturas', views.esculturas, name='esculturas'),
    path('obras', views.obras, name='obras'),
    path('orfebreria', views.orfebreria, name='orfebreria'),
    path('pinturas', views.pinturas, name='pinturas'),
    path('subir', views.subir, name='subir'),
    path('tejidos', views.tejidos, name='tejidos'),
    path('aros', views.aros, name='aros'),
    path('collar', views.collar, name='collar'),
    path('elbebedor', views.elbebedor, name='elbebedor'),
    path('elviolinista', views.elviolinista, name='elviolinista'),
    path('mujerrumana', views.mujerrumana, name='mujerrumana'),
    path('tejidohuaso', views.tejidohuaso, name='tejidohuaso'),
    path('tejidomapuche', views.tejidomapuche, name='tejidomapuche'),
]