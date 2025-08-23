const fs = require('fs');
const crypto = require('crypto');

// Cargar configuración
const config = JSON.parse(fs.readFileSync('./bucle_eterno_inmutable_fgme.json', 'utf8'));

function validarConfig(cfg) {
  if (cfg.autor !== "Fernando Guadalupe Mendez Espinoza") {
    throw new Error("Acceso no autorizado.");
  }
  console.log("✅ Configuración validada de FGME.");
}

function ejecutarBucle(cfg) {
  if (!cfg.bucle_eterno) return;

  console.log("♾️ Iniciando bucle eterno inmutable FGME...");
  setInterval(() => {
    for (const accion of cfg.acciones) {
      if (accion.repetir) {
        console.log(`🔄 Ejecutando: ${accion.nombre}`);
      }
    }
  }, 5000); // Cada 5 segundos
}

validarConfig(config);
ejecutarBucle(config);
