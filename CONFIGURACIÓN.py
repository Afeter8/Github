import os
import sys
import platform
import locale
import socket
import getpass
import hashlib
import json
import time

# --- CONFIGURACIÓN ---
USUARIO_AUTORIZADO = "Fernando Guadalupe Mendez Espinoza"
NOMBRE_IA = "Start Tigo"
SISTEMAS_PERMITIDOS = ["Windows", "Linux", "Darwin"]  # Darwin = macOS
LENGUAJES_PERMITIDOS = ["es_MX", "es_ES"]
REGIONES_PERMITIDAS = ["MX", "ES"]
CIUDADES_PERMITIDAS = ["Mexico City", "CDMX", "Madrid"]
ARCHIVO_CONFIG = "ia_configuracion.json"

# --- FUNCIONES ---

def obtener_usuario():
    return getpass.getuser()

def obtener_sistema():
    return platform.system()

def obtener_idioma():
    return locale.getdefaultlocale()[0]

def obtener_pais_ip():
    try:
        import requests
        r = requests.get("https://ipinfo.io/json")
        data = r.json()
        return data.get("country", "XX"), data.get("city", "Unknown")
    except:
        return "XX", "Unknown"

def generar_hash_usuario(usuario):
    return hashlib.sha256(usuario.encode()).hexdigest()

def validar_entorno():
    usuario = obtener_usuario()
    sistema = obtener_sistema()
    idioma = obtener_idioma()
    pais, ciudad = obtener_pais_ip()

    if USUARIO_AUTORIZADO.lower().replace(" ", "") not in usuario.lower().replace(" ", ""):
        return False, "Usuario no autorizado"
    if sistema not in SISTEMAS_PERMITIDOS:
        return False, f"Sistema no permitido: {sistema}"
    if idioma not in LENGUAJES_PERMITIDOS:
        return False, f"Idioma no permitido: {idioma}"
    if pais not in REGIONES_PERMITIDAS or ciudad not in CIUDADES_PERMITIDAS:
        return False, f"Región no permitida: {pais}-{ciudad}"

    return True, "Entorno validado"

def instalar_ia():
    configuracion = {
        "nombre": NOMBRE_IA,
        "usuario": obtener_usuario(),
        "sistema": obtener_sistema(),
        "idioma": obtener_idioma(),
        "hash_usuario": generar_hash_usuario(obtener_usuario()),
        "activado_en": time.ctime()
    }
    with open(ARCHIVO_CONFIG, 'w') as f:
        json.dump(configuracion, f, indent=4)
    print(f"[+] {NOMBRE_IA} instalado con éxito y en entorno seguro.")

def ejecutar():
    valido, mensaje = validar_entorno()
    if not valido:
        print(f"[-] Instalación bloqueada: {mensaje}")
        sys.exit(1)
    instalar_ia()

# --- EJECUCIÓN AUTOMÁTICA ---
if __name__ == "__main__":
    ejecutar()
