import imp
from django.urls import path , include
from .import views
from rest_framework import routers
# from views import home


router = routers.DefaultRouter()
router.register('producto', views.ProductoViewSet)

urlpatterns = [
    path('', views.home , name="home"),
    path('contacto/', views.contacto , name="contacto"),
    path('galeria/', views.galeria , name="galeria"),
    path('agregar-producto/', views.agregar_producto , name="agregar_producto"),
    path('listar-producto/', views.listar_producto , name="listar_producto"),
    path('editar-producto/<id>/', views.editar_producto , name="editar_producto"),
    path('eliminar-producto/<id>/', views.eliminar_producto , name="eliminar_producto"),
    path('eliminar-producto/<id>/', views.eliminar_producto , name="eliminar_producto"),
    path('registro/', views.registro , name="registro"),
    path('api/', include(router.urls)),

]
