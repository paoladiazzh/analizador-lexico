**S** → `bof` **PROGRAMA** `eof`

**PROGRAMA** → **LISTADECL**

**LISTADECL** → **DECL** **LISTADECL** | ε

**DECL** → **DECLVAR** | **DECLFUNC**

**DECLVAR** → **TIPO** **LISTAID** `puntoycoma`

**LISTAID** → `id` | `id` `coma` **LISTAID**

**TIPO** → `int` | `float` | `void`

**DECLFUNC** → **TIPO** `id` `lparen` **PARAMETROS** `rparen` **BLOQUE**  
 | **TIPO** `id` `lparen` `rparen` **BLOQUE**

**PARAMETROS** → **PARAMLISTA** | ε

**PARAMLISTA** → **PARAM** | **PARAM** `coma` **PARAMLISTA**

**PARAM** → **TIPO** `id`

**BLOQUE** → `lbrace` **LISTASENTENCIAS** `rbrace`

**LISTASENTENCIAS** → **SENTENCIA** **LISTASENTENCIAS** | ε

**SENTENCIA** → **SENTENCIAEXPR**  
 | **SENTENCIASEL**  
 | **SENTENCIAITER**  
 | **SENTENCIARET**  
 | **SENTENCIAPRINT**  
 | **BLOQUE**

**SENTENCIAEXPR** → **ASIGNACION** `puntoycoma` | `puntoycoma`

**ASIGNACION** → `id` `asignacion` **EXPR** | **EXPR**

**SENTENCIASEL** → `if` `lparen` **EXPR** `rparen` **SENTENCIA**  
 | `if` `lparen` **EXPR** `rparen` **SENTENCIA** `else` **SENTENCIA**

**SENTENCIAITER** → `while` `lparen` **EXPR** `rparen` **SENTENCIA**  
 | `for` `lparen` **EXPR** `puntoycoma` **EXPR** `puntoycoma` **EXPR** `rparen` **SENTENCIA**

**SENTENCIARET** → `return` **EXPR** `puntoycoma`

**SENTENCIAPRINT** → `print` `lparen` **EXPR** `rparen` `puntoycoma`

**EXPR** → **EXPR** `op_or` **EXPRAND** | **EXPRAND**

**EXPRAND** → **EXPRAND** `op_and` **EXPREQ** | **EXPREQ**

**EXPREQ** → **EXPREQ** (`op_eq` | `op_neq`) **EXPRREL** | **EXPRREL**

**EXPRREL** → **EXPRREL** (`op_lt` | `op_gt` | `op_le` | `op_ge`) **EXPRADIT** | **EXPRADIT**

**EXPRADIT** → **EXPRADIT** (`op_suma` | `op_resta`) **TERM** | **TERM**

**TERM** → **TERM** (`op_mul` | `op_div` | `op_mod`) **FACTOR** | **FACTOR**

**FACTOR** → `lparen` **EXPR** `rparen`  
 | `id`  
 | `num`  
 | `op_not` **FACTOR**  
 | `id` `lparen` **ARGLIST** `rparen`  
 | `id` `lparen` `rparen`

**ARGLIST** → **EXPR** | **EXPR** `coma` **ARGLIST**
