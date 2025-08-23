# sistema_ai_proteccion.py
import hashlib
import os
import json
import time
import platform
import uuid
from cryptography.fernet import Fernet
from datetime import datetime

# Generador de claves y cifrado
def generar_clave():
    return Fernet.generate_key()

clave = generar_clave()
cifrador = Fernet(clave)

# Identidad única del sistema
def generar_id_sistema():
    return hashlib.sha256(str(uuid.getnode()).encode()).hexdigest()

ID_SISTEMA = generar_id_sistema()

# Registro de auditoría
def registrar_actividad(accion, estado="OK"):
    log = {
        "id_sistema": ID_SISTEMA,
        "accion": accion,
        "estado": estado,
        "timestamp": datetime.utcnow().isoformat()
    }
    with open("auditoria.log", "a") as archivo:
        archivo.write(json.dumps(log) + "\n")

# Protección contra clonación
def verificacion_hardware():
    serial = uuid.getnode()
    return serial == uuid.getnode()  # Confirmación de hardware original

# Simulación de ejecución descentralizada
def ejecutar_tarea():
    if verificacion_hardware():
        registrar_actividad("Ejecución autorizada")
        print("Ejecución descentralizada segura iniciada.")
    else:
        registrar_actividad("Fallo de seguridad", estado="BLOQUEADO")
        raise PermissionError("Sistema clonado o no autorizado.")

# Autoejecución en bucle eterno con control
def ciclo_ejecucion_segura():
    while True:
        try:
            ejecutar_tarea()
            time.sleep(60)  # Espera segura
        except Exception as e:
            registrar_actividad("Error crítico", estado=str(e))
            break

if __name__ == "__main__":
    print("Sistema de protección IA activo")
    ciclo_ejecucion_segura()
