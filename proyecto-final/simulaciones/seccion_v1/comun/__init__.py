"""Infraestructura compartida del protocolo v2.

Contiene SOLO codigo puro y utilidades de E/S. Ningun modulo de aqui guarda
resultados de simulacion en memoria entre pasos: el unico canal entre pasos es
el contrato JSON en disco (ver `almacen.py`).
"""
import os

# El repositorio vive en WSL y Lumerical en Windows, asi que el Python que
# ejecuta los pasos escribe en \\wsl.localhost\... Sobre esa UNC el bloqueo de
# archivos de HDF5 falla con "unable to lock file, errno = 2". Desactivarlo es
# seguro aqui: un solo proceso escribe cada HDF5 en cada momento.
os.environ.setdefault("HDF5_USE_FILE_LOCKING", "FALSE")
