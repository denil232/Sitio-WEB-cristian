import os
import django

# --- 1. CONFIGURACIÓN DE DJANGO (Para que funcione sin el servidor) ---
# Asumo que tu carpeta de configuración se llama 'sitioweb' por tus mensajes anteriores
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitioweb.settings')
django.setup()

# Ahora sí podemos importar los modelos
from django.core.files import File
from django.conf import settings
from core.models import Obra

# --- 2. RUTA DE TUS IMÁGENES (La que vimos en tu captura) ---
ruta_imagenes = r"C:\Users\ASUS\Desktop\Sitio-WEB-cristian\core\static\core"

print(f"--> Buscando imágenes en: {ruta_imagenes}")

# --- 3. DATOS DE LAS OBRAS ---
datos = [
    {"t": "GUIÑA CANELO FLOR DE HUAIRAVO", "img": "imagen1disponible.png", "e": "disponible", "d": "La guiña es silenciosa y hermosa, le brota un canelo que oculta huairavos de amor."},
    {"t": "DEL MONTE CHILCO", "img": "imagen2disponible.png", "e": "disponible", "d": "El monito del monte se posa sobre la raíz caída y desde su fuerza hace crecer un chilco."},
    {"t": "CACTÁCEA DE MARINO", "img": "imagen3disponible.png", "e": "disponible", "d": "El lobito se detiene a descansar en el roquerío hasta hacer crecer el cacto rosa."},
    {"t": "PEUMO DEL PANTANO", "img": "imagen4disponible.png", "e": "disponible", "d": "El cuervo del pantano brilla de esplendor tornasol y al abrir sus alas florece la flor del peumo."},
    {"t": "CORAL DE PIQUERO", "img": "imagen5disponible.png", "e": "disponible", "d": "El piquero toma altura y se sumerge en las profundidades del mar para anidar en el hermoso coral."},
    {"t": "CHUNGUNGO DE HUIRO", "img": "imagen6disponible.png", "e": "disponible", "d": "El chungungo le dice no a la desaparición del huiro, así que lo lleva a todas partes."},
    {"t": "OBRA RESERVADA 1", "img": "imagen1reservado.png", "e": "reservado", "d": "Esta obra se encuentra actualmente reservada por un coleccionista de arte."},
    {"t": "OBRA RESERVADA 2", "img": "imagen2reservado.png", "e": "reservado", "d": "Esta pieza se encuentra apartada temporalmente por un comprador interesado."},
    {"t": "OBRA VENDIDA 1", "img": "imagen1vendido.png", "e": "vendido", "d": "Esta obra fue adquirida por un coleccionista particular."},
    {"t": "OBRA VENDIDA 2", "img": "imagen2vendido.png", "e": "vendido", "d": "Vendida durante la exposición en la Sala de Obras."}
]

# --- 4. PROCESO DE GUARDADO ---
print("--> Iniciando la carga de datos a la base de datos...")

contador = 0
for item in datos:
    # Verificamos si ya existe para no duplicar
    if not Obra.objects.filter(titulo=item['t']).exists():
        archivo_completo = os.path.join(ruta_imagenes, item['img'])
        
        if os.path.exists(archivo_completo):
            try:
                with open(archivo_completo, 'rb') as f:
                    nueva = Obra(titulo=item['t'], descripcion=item['d'], estado=item['e'])
                    nueva.imagen.save(item['img'], File(f), save=True)
                    contador += 1
                    print(f"   [OK] Guardada: {item['t']}")
            except Exception as e:
                print(f"   [ERROR] Falló al guardar {item['t']}: {e}")
        else:
            print(f"   [AVISO] No encontré la imagen: {item['img']} en la carpeta.")
    else:
        print(f"   [SALTADO] Ya existe: {item['t']}")

print(f"\n--> ¡LISTO! Se agregaron {contador} obras nuevas.")