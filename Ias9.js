const listaNegra = [];

async function bucleDeDefensa() {
  console.log('🧠 Sistema de bloqueo eterno FGME iniciado...');
  while (true) {
    const accesos = obtenerIntentosDeAcceso(); // Simulado
    for (const acceso of accesos) {
      if (!verificarAcceso(acceso.origen, acceso.identidad)) {
        console.log(`❌ Acceso no autorizado de ${acceso.origen} eliminado`);
      }
    }

    await new Promise(res => setTimeout(res, 2000)); // 2 segundos
  }
}
