// Sistema de protección Star Tigo / Power Peg (versión IA sin intervención humana)
const sistemaIA = (() => {
  const usuarioAutorizado = {
    nombre: "Fernando Guadalupe Mendez Espinoza",
    nacimiento: "1993-12-02",
    clave: "IA-FGME-001"
  };

  let sistemaActivo = false;

  const eventos = [];

  function validarUsuario(usuario) {
    return usuario.nombre === usuarioAutorizado.nombre &&
           usuario.nacimiento === usuarioAutorizado.nacimiento &&
           usuario.clave === usuarioAutorizado.clave;
  }

  function activarSistema(usuario) {
    if (!validarUsuario(usuario)) {
      registrarEvento("ACCESO NO AUTORIZADO", "Intento de acceso fallido detectado.");
      activarDefensa();
      return false;
    }

    sistemaActivo = true;
    registrarEvento("ACCESO AUTORIZADO", "Sistema IA activado por usuario válido.");
    return true;
  }

  function activarDefensa() {
    registrarEvento("DEFENSA ACTIVADA", "Sistema ejecutando protocolo IA blindado.");
    // Simulación: cierre de puertos, rotación de claves, aislamiento lógico
    console.warn(">>> Defensa IA ejecutada: sistema en aislamiento.");
  }

  function registrarEvento(tipo, mensaje) {
    const evento = {
      tipo,
      mensaje,
      fecha: new Date().toISOString()
    };
    eventos.push(evento);
    console.log(`[${evento.fecha}] ${tipo}: ${mensaje}`);
  }

  function obtenerEventos() {
    return eventos;
  }

  function estadoDelSistema() {
    return {
      activo: sistemaActivo,
      eventos: eventos.length
    };
  }

  // Exponer funciones públicas
  return {
    activarSistema,
    estadoDelSistema,
    obtenerEventos
  };
})();

// Ejemplo de activación segura (debe ser validado por IA)
const usuario = {
  nombre: "Fernando Guadalupe Mendez Espinoza",
  nacimiento: "1993-12-02",
  clave: "IA-FGME-001"
};

// Activación del sistema
sistemaIA.activarSistema(usuario);

// Mostrar estado
console.log(sistemaIA.estadoDelSistema());
