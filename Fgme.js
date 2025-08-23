function protegerNombre(codigo) {
  const nombreOriginal = "Fernando Guadalupe Mendez Espinoza";
  if (!codigo.includes(nombreOriginal)) {
    throw new Error("❌ Código sin autorización de nombre FGME detectado.");
  }
  return true;
}
