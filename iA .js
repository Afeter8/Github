class SistemaDefensaIA {
  constructor() {
    this.listaNegraIPs = new Set();
    this.eventos = [];
  }

  detectarAnomalia(evento) {
    // Ejemplo simple: detectar intentos múltiples fallidos
    if(evento.tipo === 'login-fallido' && evento.intentos > 5) {
      this.bloquearIP(evento.ip);
    }
  }

  bloquearIP(ip) {
    if(!this.listaNegraIPs.has(ip)) {
      this.listaNegraIPs.add(ip);
      console.log(`[DEFENSA IA] IP bloqueada automáticamente: ${ip}`);
      // Implementar bloqueo real en firewall o sistema
    }
  }

  monitorearEventos() {
    // Simulación: Escuchar eventos (logs, accesos, cambios)
    setInterval(() => {
      const eventoSimulado = this.generarEventoSimulado();
      this.detectarAnomalia(eventoSimulado);
      this.registrarEvento(eventoSimulado);
    }, 1000);
  }

  registrarEvento(evento) {
    this.eventos.push({...evento, timestamp: new Date()});
    // Aquí se podría enviar a blockchain o almacenamiento seguro
  }

  generarEventoSimulado() {
    // Genera eventos falsos para demo
    return {
      tipo: 'login-fallido',
      intentos: Math.floor(Math.random() * 10),
      ip: `192.168.1.${Math.floor(Math.random() * 255)}`
    };
  }

  iniciarBucleEterno() {
    console.log('[DEFENSA IA] Iniciando sistema de defensa en bucle eterno...');
    this.monitorearEventos();
  }
}

// Crear instancia y arrancar
const defensa = new SistemaDefensaIA();
defensa.iniciarBucleEterno();
