from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# IMPORTANTE: Esto es necesario para que funcione el cambio de contraseña
from django.contrib.auth import views as auth_views 
from core import views

urlpatterns = [
    # --- VISTAS PÚBLICAS ---
    path('', views.home, name='home'),
    path('galeria/', views.galeria, name='galeria'),
    path('preguntas/', views.preguntas, name='preguntas'),
    path('quienes/', views.quienes, name='quienes'),
    path('contacto/', views.contacto, name='contacto'),

    # --- VISTAS DE GESTIÓN (Staff/Cristian) ---
    path('galeria/agregar/', views.agregar_obra, name='agregar_obra'),
    path('galeria/editar/<int:obra_id>/', views.editar_obra, name='editar_obra'),
    path('galeria/eliminar/<int:obra_id>/', views.eliminar_obra, name='eliminar_obra'),

    # --- AUTENTICACIÓN PERSONALIZADA (Tus diseños bonitos) ---
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),

    # --- RECUPERACIÓN DE CONTRASEÑA (Sistema Gmail) ---
    # 1. Formulario para pedir el correo
    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="core/password/password_reset_form.html"), 
         name='password_reset'),

    # 2. Mensaje de "Correo enviado exitosamente"
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="core/password/password_reset_done.html"), 
         name='password_reset_done'),

    # 3. Link especial que llega al correo para poner la nueva clave
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name="core/password/password_reset_confirm.html"), 
         name='password_reset_confirm'),

    # 4. Mensaje de "Contraseña cambiada correctamente"
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="core/password/password_reset_complete.html"), 
         name='password_reset_complete'),

    path('admin/', admin.site.urls),
]

# Configuración para ver imágenes en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)