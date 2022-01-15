import imp
from django.urls import path
from .import views
# from views import home


urlpatterns = [
    path('', views.home , name="home"),
    path('contacto/', views.contacto , name="contacto"),
    path('galeria/', views.galeria , name="galeria"),
    path('agregar-producto/', views.agregar_producto , name="agregar_producto"),
    path('listar-producto/', views.listar_producto , name="listar_producto"),
]
