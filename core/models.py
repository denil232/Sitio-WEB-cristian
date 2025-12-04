from django.db import models

class Obra(models.Model):
    # Opciones para el estado de la obra
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('vendido', 'Vendido'),
    ]

    titulo = models.CharField(max_length=100, verbose_name="Título de la obra")
    descripcion = models.TextField(verbose_name="Descripción", blank=True)
    imagen = models.ImageField(upload_to='obras/', verbose_name="Foto de la obra")
    
    # ELIMINADO: Campo precio
    
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Obra de Arte"
        verbose_name_plural = "Galería de Obras"
        # Esto ordena las obras para que las más nuevas aparezcan primero automáticamente
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.titulo} ({self.estado})"