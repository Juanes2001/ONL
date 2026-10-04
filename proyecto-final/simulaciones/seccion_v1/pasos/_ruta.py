"""Preparacion comun a todos los pasos, antes de cualquier otro import.

1. Deja el paquete raiz en sys.path para que cada paso se pueda correr suelto:
       python pasos/paso01_ancho_sensor.py
2. Fuerza UTF-8 en la salida. Los pasos se ejecutan con el Python de Windows
   (es el unico que ve lumapi) y su consola por defecto es cp1252, que destroza
   los acentos y los caracteres de las tablas. PYTHONIOENCODING no sirve aqui:
   al lanzar un binario de Windows desde WSL las variables de entorno de Linux
   no llegan al hijo salvo que esten en WSLENV.
"""
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
if str(RAIZ) not in sys.path:
    sys.path.insert(0, str(RAIZ))

for flujo in (sys.stdout, sys.stderr):
    try:
        flujo.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
