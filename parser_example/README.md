# Parser - Analizador Sintáctico

## Características
- Implementación con **clase `Parser`**.
- Soporta expresiones con:
  - Operadores aritméticos: `+`, `-`, `*`, `/`
  - Identificadores y números
  - Paréntesis `()` y corchetes `[]`
- El código fuente se lee desde un archivo `.txt`.

## Archivos del Proyecto
- `parser.py` → Implementación del analizador.
- `caso_exito.txt` → Archivo de ejemplo válido.
- `caso_falla.txt` → Archivo de ejemplo con error de sintaxis.
- `README.md` → Documentación del proyecto.

## Ejemplo de Uso

1. Ejecutar el parser indicando un archivo válido:

   ```bash
   python parser.py caso_exito.txt
   ```

   Resultado esperado:
   ```bash
   Parsing completed :)
   ```

2. Ejecutar el parser con un archivo con error de sintaxis:

   ```bash
   python parser.py caso_falla.txt
   ```

   Resultado esperado:
   ```bash
   Syntax error :(
   ```
