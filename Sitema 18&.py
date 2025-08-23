import hashlib
import getpass
import platform
import sys
import os
import time

# --- CONFIGURACIÓN ---
AUTORIZADO = "Fernando Guadalupe Mendez Espinoza"
HASH_ARCHIVO_ORIGINAL = "a1f3..."  # <- Reemplaza esto con el hash real luego de crear el archivo

# --- FUNCIONES ---

def obtener_identidad_usuario():
    return getpass.getuser() + "-" + platform.node()

def calcular_hash_archivo(ruta):
    sha256 = hashlib.sha256()
    with open(ruta, 'rb') as f:
        for bloque in iter(lambda: f.read(4096), b""):
            sha256.update(bloque)
    return sha256.hexdigest()

def verificar_integridad():
    ruta = os.path.abspath(__file__)
    hash_actual = calcular_hash_archivo(ruta)
    return hash_actual == HASH_ARCHIVO_ORIGINAL

def verificar_identidad():
    identidad = obtener_identidad_usuario()
    return AUTORIZADO.lower().replace(" ", "") in identidad.lower().replace(" ", "")

def activar_sistema():
    print("[+] Sistema Start Tigo: Protección Activa")
    print(f"[+] Usuario autorizado: {AUTORIZADO}")
    # Aquí puedes lanzar la IA, interfaz o tareas automáticas
    time.sleep(3)

def bloquear_sistema():
    print("[-] ALERTA: Acceso no autorizado o modificación detectada")
    print("[-] Bloqueando sistema...")
    time.sleep(3)
    sys.exit(1)

# --- EJECUCIÓN AUTOMÁTICA ---
if __name__ == "__main__":
    if verificar_identidad() and verificar_integridad():
        activar_sistema()
    else:
        bloquear_sistema()
