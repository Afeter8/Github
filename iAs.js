function esIdentidadAutorizada(identidad) {
  const huellaFGME = "FGME_1987_AUTH_KEY_∞";
  return identidad === huellaFGME;
}

function bloquearIntruso(origen) {
  console.warn(`🛑 Bloque permanente activado para: ${origen}`);
  // Desconectar sesión, cerrar puertos, eliminar procesos, bloquear IP
  listaNegra.push(origen);
}

function verificarAcceso(origen, identidad) {
  if (!esIdentidadAutorizada(identidad)) {
    bloquearIntruso(origen);
    return false;
  }
  return true;
}
