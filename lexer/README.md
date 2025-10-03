# Analizador Léxico en Python

Este proyecto consiste en la implementación de un **analizador léxico** en Python que utiliza **Autómatas Finitos** para reconocer los tokens de un lenguaje definido previamente.  

---

## Propuesta de palabras clave

El lenguaje definido incluye palabras reservadas como `if`, `else`, `while`, `for`, `int`, `float`, `return`, `print`, `void`, entre otras.  
Además, reconoce identificadores, números, operadores aritméticos, relacionales, lógicos, y delimitadores.  

---

## Definición formal de tokens con expresiones regulares

La definición completa de tokens, junto con sus expresiones regulares y ejemplos, se encuentra en el archivo:  
[`tokens_spec.md`](tokens_spec.md)

---

## Autómata Finito No Determinista (AFND)

El diseño inicial del analizador se basa en un **AFND**, que permite modelar de forma flexible los posibles caminos de reconocimiento de cada token.  
El diagrama correspondiente se encuentra en el siguiente enlace:  
[Diagrama AFND](https://lucid.app/lucidchart/a78871ba-7cc3-4caa-8c53-7844edf057fe/edit?viewport_loc=-321%2C-481%2C2843%2C3841%2C0_0&invitationId=inv_c09519fa-bb1f-4fff-a7e1-1896efd43043)

---

## Autómata Finito Determinista (AFD)

Posteriormente, el AFN es transformado en un **AFD**, que permite la implementación eficiente del analizador al garantizar transiciones únicas por cada símbolo de entrada.  
El diagrama se encuentra disponible en:  
[Diagrama AFD](https://lucid.app/lucidchart/20b62fa0-a7ab-4bdb-b0de-ef1500914efa/edit?viewport_loc=-240%2C-1076%2C3881%2C5244%2C0_0&invitationId=inv_9e8aec8e-bcec-4355-846e-90e47b2bb4c7)

---

## Breve descripción del diseño del analizador

El analizador léxico (`lexer.py`) sigue el siguiente enfoque:

1. **Lectura del código fuente** desde un archivo (ejemplo: `sample.src`).  
2. **Normalización del código** mediante la función `limpiar_codigo`, que elimina comentarios y espacios innecesarios.  
3. **Reconocimiento de tokens** usando:
   - Autómatas para identificadores y números.
   - Tablas de operadores de uno y dos caracteres.
   - Validación contra palabras clave.  
4. **Construcción de la lista de tokens** que será utilizada en fases posteriores del compilador/intérprete.  
5. **Manejo de errores léxicos**: si se encuentra un carácter inválido, se lanza una excepción `LexerError`.

## Casos de prueba

- [sample2.src](sample2.src) – Caso de éxito.  

- [sample3.src](sample3.src) – Caso de éxito.  

- [sample4.src](sample4.src) – Caso de falla: Lexema inválido.  

- [sample5.src](sample5.src) – Caso de falla: carácter inválido.  

Ejemplo de ejecución:  

```bash
python lexer.py sample.src
