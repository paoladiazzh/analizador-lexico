S → BOF Programa EOF
Programa      -> ListaDecl
ListaDecl     -> Decl ListaDecl| ε
Decl          -> DeclVar | DeclFunc
DeclVar       -> Tipo ListaId PUNTOYCOMA
ListaId       -> ID | ID COMA ListaId
Tipo          -> INT | FLOAT
DeclFunc      -> Tipo ID LPAREN Parametros RPAREN Bloque | Tipo ID LPAREN RPAREN Bloque
Parametros    -> ParamLista | ε
ParamLista    -> Param | Param COMA ParamLista
Param         -> Tipo ID
Bloque        -> LBRACE ListaSentencias RBRACE
ListaSentencias -> Sentencia ListaSentencias | ε
Sentencia     -> SentenciaExpr | SentenciaSel | SentenciaIter | SentenciaRet | SentenciaPrint | Bloque
SentenciaExpr -> Expr PUNTOYCOMA | PUNTOYCOMA
SentenciaSel  -> IF LPAREN Expr RPAREN Sentencia | IF LPAREN Expr RPAREN Sentencia ELSE Sentencia
SentenciaIter -> WHILE LPAREN Expr RPAREN Sentencia | FOR LPAREN Expr PUNTOYCOMA Expr PUNTOYCOMA Expr RPAREN Sentencia
SentenciaRet  -> RETURN Expr PUNTOYCOMA
SentenciaPrint -> PRINT LPAREN Expr RPAREN PUNTOYCOMA
Expr          -> Expr OP_OR ExprAnd | ExprAnd
ExprAnd       -> ExprAnd OP_AND ExprEq | ExprEq
ExprEq        -> ExprEq (OP_EQ | OP_NEQ) ExprRel | ExprRel
ExprRel       -> ExprRel (OP_LT | OP_GT | OP_LE | OP_GE) ExprAdit | ExprAdit
ExprAdit      -> ExprAdit (OP_SUMA | OP_RESTA) Term | Term
Term          -> Term (OP_MUL | OP_DIV | OP_MOD) Factor | Factor
Factor        -> LPAREN Expr RPAREN | ID | NUM | OP_NOT Factor | ID LPAREN ArgList RPAREN | ID LPAREN RPAREN
ArgList       -> Expr | Expr COMA ArgList
