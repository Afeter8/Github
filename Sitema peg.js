(function () {
  const estado = document.getElementById('estado');

  // Clave digital de identidad (simulación para Fernando)
  const CLAVE_FERNANDO = btoa("Fernando_Guadalupe_Mendez_Espinoza");

  // Genera huella digital simple del sistema
  function generarHuella() {
    return btoa(navigator.userAgent + navigator.platform + navigator.language);
  }

  // Verifica si la huella contiene la clave válida
  function verificarIdentidad() {
    const huella = generarHuella();
    return huella.includes(CLAVE_FERNANDO);
  }

  // Detección de manipulación del código (checksum simulado)
  function verificarIntegridad() {
    const html = document.documentElement.innerHTML;
    let checksum = 0;
    for (let i = 0; i < html.length; i++) {
      checksum += html.charCodeAt(i);
    }
    return (checksum % 9973) === 777; // Valor arbitrario como hash
  }

  // Acción si hay error o alteración
  function bloquearAcceso() {
    document.body.classList.add("error");
    estado.textContent = "ACCESO BLOQUEADO: Identidad o integridad comprometida.";
    setTimeout(() => window.close(), 3000);
  }

  // Acción permitida
  function accesoPermitido() {
    document.body.classList.add("ok");
    estado.textContent = "Acceso autorizado. Sistema Start Tigo en modo seguro.";
  }

  // Autoejecución
  if (!verificarIdentidad() || !verificarIntegridad()) {
    bloquearAcceso();
  } else {
    accesoPermitido();
  }
})();
