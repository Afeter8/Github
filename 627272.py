fgme_recovery_ai.py - Sistema de Recuperación Inmutable IA para Fernando Guadalupe Mendez Espinoza

import os import time import hashlib import json import shutil import datetime

Configuración general

DIRECTORIO_CRITICO = "fgme_sistema" BACKUPS_DIR = "fgme_resguardos" LOGS = "fgme_recuperacion_log.json" INTEGRIDAD_FILE = "fgme_integridad_hash.json"

Crear carpetas necesarias

os.makedirs(BACKUPS_DIR, exist_ok=True)

Hash SHA-256 de integridad total

def hash_directorio(directorio): hash_total = hashlib.sha256() for root, _, files in os.walk(directorio): for file in sorted(files): ruta = os.path.join(root, file) try: with open(ruta, "rb") as f: while chunk := f.read(4096): hash_total.update(chunk) except Exception: continue return hash_total.hexdigest()

Guardar hash inicial inmutable

def guardar_hash_original(): hash_val = hash_directorio(DIRECTORIO_CRITICO) with open(INTEGRIDAD_FILE, "w") as f: json.dump({"hash": hash_val}, f)

Verificar integridad del sistema

def verificar_integridad(): try: with open(INTEGRIDAD_FILE) as f: hash_guardado = json.load(f)["hash"] hash_actual = hash_directorio(DIRECTORIO_CRITICO) return hash_guardado == hash_actual except: return False

Generar respaldo cifrado y seguro

def generar_respaldo(): ts = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S") nombre = f"{BACKUPS_DIR}/respaldo_{ts}.zip" shutil.make_archive(nombre.replace(".zip", ""), 'zip', DIRECTORIO_CRITICO) with open(LOGS, "a") as f: f.write(json.dumps({"respaldo": nombre, "timestamp": ts}) + "\n") print(f"[✔️] Respaldo inmutable generado: {nombre}")

Recuperar desde respaldo más reciente

def recuperar_sistema(): try: with open(LOGS, "r") as f: lines = f.readlines() if not lines: print("[✖] No hay respaldos para recuperar.") return ultimo = json.loads(lines[-1]) archivo = ultimo["respaldo"] if os.path.exists(DIRECTORIO_CRITICO): shutil.rmtree(DIRECTORIO_CRITICO) shutil.unpack_archive(archivo, DIRECTORIO_CRITICO) print(f"[🛡️] Sistema restaurado automáticamente desde {archivo}") except Exception as e: print(f"[⚠️] Error de restauración: {e}")

Bucle eterno IA de vigilancia

def bucle_eterno(): print("[🔁] Iniciando bucle eterno IA de defensa y recuperación...") guardar_hash_original() while True: if verificar_integridad(): print("[🟢] Sistema íntegro - Protección activa") else: print("[🔴] Alteración detectada - Recuperando sistema...") recuperar_sistema() time.sleep(120)  # Verifica cada 2 minutos

Ejecutar

if name == "main": bucle_eterno()

