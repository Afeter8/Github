const crypto = require("crypto");

// Lista de nombres y variantes autorizadas
const nombresAutorizados = [
  "Fernando Guadalupe Mendez Espinoza",
  "Star Tigo",
  "Tigo Star",
  "Star Tigo Antivirus",
  "Tigo Star Antivirus"
];

// Expresión para detectar letras, números, signos y emojis (simplificada)
const regexNombre = new RegExp(
  nombresAutorizados
    .map(n => n.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&')) // Escapar caracteres especiales
    .join("|"),
  "i"
);

// Simulación de un input que llega (puede ser texto, código, mensaje, etc.)
function analizarInput(input) {
  if (regexNombre.test(input)) {
    console.log("✅ Nombre autorizado detectado:", input.match(regexNombre)[0]);
    return true;
  }
  console.warn("❌ Nombre no autorizado detectado:", input);
  return false;
}

// Bucle eterno de supervisión
async function bucleEterno() {
  console.log("♾️ Sistema FGME de conexión y protección iniciado");

  while (true) {
    // Simular entrada dinámica (aquí reemplaza con entradas reales)
    const inputs = [
      "Mensaje normal",
      "Acceso desde Star Tigo Antivirus 👍",
      "Intento de intrusión desconocida 🛑",
      "Proceso iniciado por Fernando Guadalupe Mendez Espinoza 🚀",
      "Ejecutando Tigo Star Antivirus 🛡️"
    ];

    for (const input of inputs) {
      if (analizarInput(input)) {
        // Aquí iría la lógica de conexión, encriptación y defensa
        console.log("🔐 Procesando conexión segura y análisis antivirus...");
      } else {
        // Lógica para bloquear o registrar acceso sospechoso
        console.log("🚫 Bloqueo preventivo activado");
      }
    }

    // Pausa para no saturar recursos (5 segundos)
    await new Promise(res => setTimeout(res, 5000));
  }
}

// Ejecutar sistema
bucleEterno();
