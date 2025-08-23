import json

def cargar_configuracion(path="defensa_telecom.json"):
    with open(path, "r") as archivo:
        return json.load(archivo)

def validar_usuario(usuario, config):
    return usuario == config["usuario_autorizado"]["nombre"]

def accion_intrusion_detectada(config):
    if config["acciones_ante_intrusion"]["generar_error_modem"]:
        print("Error crítico de red generado")
    if config["acciones_ante_intrusion"]["bloquear_red_temporal"]:
        print("Red bloqueada temporalmente")
    # Aquí se integrarían comandos de sistema según el OS
    # Para Linux: subprocess + iptables, rfkill, etc.

def recuperar_sistema(config, usuario):
    if validar_usuario(usuario, config):
        print("Acceso al sistema de recuperación autorizado")
    else:
        print("Intento no autorizado. Sistema bloqueado.")

config = cargar_configuracion()
usuario_ingresado = "Fernando Guadalupe Mendez Espinoza"
recuperar_sistema(config, usuario_ingresado)
