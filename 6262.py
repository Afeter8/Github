import hashlib
import json
import time
import os
import threading

# ===================== #
# CONFIGURACIÓN GLOBAL  #
# ===================== #

SISTEMA_FGME = {
    "usuario": "FERNANDO GUADALUPE MENDEZ ESPINOZA",
    "proyecto": "TIGO START IA DEFENSA GLOBAL",
    "modo": "inmutable",
    "intervencion": False,
    "bucle_eterno": True,
    "version": "1.0.0-eterno"
}

CÓDIGOS_ORIGINALES = {
    "watchdog.py": "def main(): print('Monitoreando integridad...')",
    "firewall_ai.py": "def proteger(): print('Bloqueando amenazas...')",
    "guardian.json": json.dumps({"integridad": "total", "verificacion": True})
}

LOG_PATH = "log_defensa.txt"


# ===================== #
# FUNCIONES DE SEGURIDAD #
# ===================== #

def hash_sha256(content):
    return hashlib.sha256(content.encode()).hexdigest()

def verificar_integridad(nombre, actual):
    original = CÓDIGOS_ORIGINALES.get(nombre)
    return hash_sha256(original) == hash_sha256(actual)

def auto_reparar(nombre):
    print(f"[⚠️] Alteración detectada en {nombre}. Reparando...")
    with open(nombre, 'w') as archivo:
        archivo.write(CÓDIGOS_ORIGINALES[nombre])
    registrar_log(f"{nombre} reparado automáticamente.")

def registrar_log(mensaje):
    with open(LOG_PATH, 'a') as log:
        log.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {mensaje}\n")

# ===================== #
# MÓDULO IA BUCLE ETERNO #
# ===================== #

def bucle_ia_eterno():
    while True:
        for archivo in CÓDIGOS_ORIGINALES:
            try:
                if not os.path.exists(archivo):
                    auto_reparar(archivo)
                else:
                    with open(archivo, 'r') as f:
                        contenido_actual = f.read()
                    if not verificar_integridad(archivo, contenido_actual):
                        auto_reparar(archivo)
                    else:
                        registrar_log(f"{archivo} verificado OK.")
            except Exception as e:
                registrar_log(f"ERROR en {archivo}: {str(e)}")
        time.sleep(180)  # Verifica cada 3 minutos

# ===================== #
# INICIO AUTOMÁTICO     #
# ===================== #

if __name__ == "__main__":
    print(f"[🔒] Sistema IA de Defensa Inmutable activado para {SISTEMA_FGME['usuario']}")
    registrar_log("Sistema iniciado en modo inmutable.")

    if SISTEMA_FGME["bucle_eterno"]:
        hilo = threading.Thread(target=bucle_ia_eterno)
        hilo.start()
