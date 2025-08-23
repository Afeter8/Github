import time
import hashlib
import os
import getpass

# 🔐 Identidad autorizada
IDENTIDAD_AUTORIZADA = "Fernando Guadalupe Mendez Espinoza"

# 📌 Protección del nombre
def verificar_autor():
    autor_sistema = IDENTIDAD_AUTORIZADA
    if autor_sistema != "Fernando Guadalupe Mendez Espinoza":
        raise PermissionError("❌ Acceso denegado. Solo FGME puede ejecutar este sistema.")
    return True

# 🔁 Acción principal en bucle eterno
def sistema_inmutable():
    print("🔁 Sistema activado correctamente para:", IDENTIDAD_AUTORIZADA)
    while True:
        try:
            # Aquí puedes ejecutar cualquier acción automatizada:
            print("✅ Ejecutando ciclo inmutable FGME...")
            
            # Seguridad mínima (protección del script)
            ruta = os.path.abspath(__file__)
            hash_archivo = calcular_hash(ruta)
            if hash_archivo != HASH_ORIGINAL:
                raise Exception("⚠️ Código modificado detectado. Deteniendo el sistema.")

            # Esperar antes del próximo ciclo (segundos)
            time.sleep(5)

        except Exception as e:
            print("❌ Error crítico:", e)
            break

# 🔒 Hash original para integridad del archivo (opcional pero recomendado)
def calcular_hash(ruta):
    with open(ruta, "rb") as archivo:
        contenido = archivo.read()
        return hashlib.sha256(contenido).hexdigest()

# 🚨 Inserta tu propio hash original aquí después de generar por primera vez
HASH_ORIGINAL = "aqui_va_tu_hash_sha256_generado_del_script"

# 🔄 Generador de hash inicial (úsalo solo una vez para registrar tu código)
def imprimir_hash_actual():
    ruta = os.path.abspath(__file__)
    print("🔐 Hash actual del sistema:", calcular_hash(ruta))

# 📍 Activador automático
if __name__ == "__main__":
    try:
        verificar_autor()
        # imprimir_hash_actual()  # Solo activa esta línea 1 vez para copiar el hash
        sistema_inmutable()
    except PermissionError as e:
        print(str(e))
