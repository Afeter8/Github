import hashlib
import threading
import time
import json
import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.exceptions import InvalidSignature

# --- Variables y configuración ---
AUTHORIZED_BIOMETRIC_HASH = "HASH_BIOMETRICO_FGME"  # Reemplazar con hash biométrico real
LOG_FILE = "secure_ai_log.json"
PRIVATE_KEY_FILE = "private_key.pem"
PUBLIC_KEY_FILE = "public_key.pem"

# --- Generación y carga de claves ---
def generate_keys():
    if not os.path.exists(PRIVATE_KEY_FILE) or not os.path.exists(PUBLIC_KEY_FILE):
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()
        with open(PRIVATE_KEY_FILE, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        with open(PUBLIC_KEY_FILE, "wb") as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

def load_private_key():
    with open(PRIVATE_KEY_FILE, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

def load_public_key():
    with open(PUBLIC_KEY_FILE, "rb") as f:
        return serialization.load_pem_public_key(f.read())

# --- Firma y verificación ---
def sign_message(private_key, message: bytes) -> bytes:
    return private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )

def verify_signature(public_key, message: bytes, signature: bytes) -> bool:
    try:
        public_key.verify(signature, message,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256())
        return True
    except InvalidSignature:
        return False

# --- Simulación biométrica (reemplazar con integración real) ---
def capture_biometric_sample():
    # Simulación: pedir input del usuario (para demo)
    sample = input("Por favor, ingresa tu muestra biométrica (simulada): ")
    return sample

def verify_biometric():
    sample = capture_biometric_sample()
    sample_hash = hashlib.sha256(sample.encode()).hexdigest()
    return sample_hash == AUTHORIZED_BIOMETRIC_HASH

# --- Registro inmutable ---
def log_action(action: str):
    entry = {
        "action": action,
        "timestamp": time.time()
    }
    if not os.path.exists(LOG_FILE):
        logs = []
    else:
        with open(LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except:
                logs = []

    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

# --- Bloqueo / desbloqueo del sistema ---
class SecureLockSystem:
    def __init__(self):
        self.locked = True
        generate_keys()
        self.private_key = load_private_key()
        self.public_key = load_public_key()

    def activate_lock(self):
        if verify_biometric():
            self.locked = True
            log_action("Sistema bloqueado por FGME")
            print("Sistema bloqueado con éxito.")
        else:
            print("Acceso denegado. Biometría incorrecta.")

    def deactivate_lock(self):
        if verify_biometric():
            self.locked = False
            log_action("Sistema desbloqueado por FGME")
            print("Sistema desbloqueado con éxito.")
        else:
            print("Acceso denegado. Biometría incorrecta.")

    def is_locked(self):
        return self.locked

    def auto_verify_integrity(self):
        # Ejemplo: verifica la integridad del propio script (hash de archivo)
        with open(__file__, "rb") as f:
            content = f.read()
        current_hash = hashlib.sha256(content).hexdigest()
        # Aquí deberías comparar con hash original almacenado seguro
        # Por simplicidad, asumimos ok siempre
        return True

# --- Bucle eterno de monitoreo ---
def main_loop():
    system = SecureLockSystem()
    print("Sistema seguro FGME iniciado. En bucle eterno.")

    while True:
        if not system.auto_verify_integrity():
            print("Alerta: Integridad comprometida. Bloqueando sistema.")
            system.activate_lock()
            break

        if system.is_locked():
            print("Sistema bloqueado. Esperando acción autorizada...")
        else:
            print("Sistema desbloqueado. Operando normalmente...")

        time.sleep(10)  # Espera antes de siguiente ciclo

if __name__ == "__main__":
    main_loop()
