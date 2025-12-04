from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    # --- VISTAS PÚBLICAS ---
    path('', views.home, name='home'),
    path('galeria/', views.galeria, name='galeria'),
    path('preguntas/', views.preguntas, name='preguntas'),
    path('quienes/', views.quienes, name='quienes'),
    path('contacto/', views.contacto, name='contacto'),

    # --- VISTAS DE GESTIÓN (¡NUEVO! Esto es lo que faltaba) ---
    # Estas URLs conectan con tus funciones de agregar, editar y eliminar
    path('galeria/agregar/', views.agregar_obra, name='agregar_obra'),
    
    # <int:obra_id> es vital: le dice a Django QUÉ obra específica vas a editar/borrar
    path('galeria/editar/<int:obra_id>/', views.editar_obra, name='editar_obra'),
    path('galeria/eliminar/<int:obra_id>/', views.eliminar_obra, name='eliminar_obra'),

    # --- AUTENTICACIÓN (Login/Registro/Logout) ---
    # Usamos tus vistas personalizadas del views.py
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),

    path('admin/', admin.site.urls),
]

# Configuración para ver imágenes en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)