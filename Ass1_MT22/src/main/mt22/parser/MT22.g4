grammar MT22;
// 2012752 - Nguyen Thanh Cong
@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}

options{
	language=Python3;
}

program:  (decl)+ EOF ;
/**************************PARSER*****************************/
decl: var_decl SEMI | func_decl;

var_decl: (IDENTIFIER COMMA var_decl COMMA expr) 
			| IDENTIFIER COLON list_type ASSIGN expr
			| IDENTIFIER (COMMA IDENTIFIER)* COLON list_type;
			
arr_type: (ARRAY LSB INT_LIT (COMMA INT_LIT)* RSB OF atomic_types)?;
atomic_types: INT | FLOAT | STR | BOOLEAN;
list_type 	: INT
			| FLOAT
			| STR
			| BOOLEAN
			| arr_type
			| VOID
			| AUTO;

para: INHERIT? OUT? IDENTIFIER COLON list_type;
para_list: (para (COMMA para)*)?;
func_decl: IDENTIFIER COLON FUNC list_type LB para_list RB (INHERIT IDENTIFIER)? block_stmt;

block_stmt: LCB stmt_vardecl* RCB;
stmt_vardecl: stmt | var_decl SEMI;
stmt: (
	assign_stmt
	| if_stmt 
	| for_stmt 
	| while_stmt 
	| do_while_stmt 
	| break_stmt
	| continue_stmt
	| return_stmt
	| call_stmt
	| block_stmt
	| expr SEMI);

if_stmt
    : IF LB expr RB
        stmt
    (ELSE
        stmt)?
    ;
for_stmt: FOR LB (assign_stmt) (COMMA expr) (COMMA expr) RB stmt;
assign_stmt: (IDENTIFIER | index_operators) ASSIGN (expr | array) SEMI?;
// assign_stmt_for: (IDENTIFIER | index_operators) ASSIGN INT_LIT;
while_stmt: WHILE expr_while stmt;
do_while_stmt: DO block_stmt WHILE LB expr_while RB SEMI;
break_stmt: BREAK SEMI;
continue_stmt: CONTINUE SEMI;
return_stmt: RETURN SEMI
			| RETURN expr SEMI;
call_stmt: IDENTIFIER LB expr_list RB SEMI;
func_call: IDENTIFIER LB expr_list RB;

/********************* BEGIN EXPRESSIONS ***********************/

expr: relation_expr DOUBLECOLON relation_expr | relation_expr;
relation_expr: logic_expr (EQUAL| NOT_EQUAL| SMALLER| BIGGER| SMALLER_OR_EQUAL| BIGGER_OR_EQUAL) logic_expr | logic_expr;
logic_expr: logic_expr (AND | OR) add_expr | add_expr;
add_expr: add_expr (ADD | SUB) mul_expr | mul_expr;
mul_expr: mul_expr (MUL | DIV | MOD) not_expr | not_expr;
not_expr: NOT not_expr | sign_expr;
sign_expr: (SUB sign_expr) | exp9;
exp9: index_operators | operand;
operand: func_call
		| IDENTIFIER
		| INT_LIT 
		| FLOAT_LIT 
		| STRING_LIT 
		| BOOL_LIT 
		| array
		| LB expr RB;
expr_list: (expr (COMMA expr)*)?;
index_operators: IDENTIFIER LSB expr_list RSB;

/******** BEGIN EXPRESSIONS WITHOUT ARRAY IN ASSIGN******************/

expr_while: relation_expr1 DOUBLECOLON relation_expr1 | relation_expr1;
relation_expr1: 
			logic_expr1 (
				EQUAL
				| NOT_EQUAL
				| SMALLER
				| BIGGER
				| SMALLER_OR_EQUAL
				| BIGGER_OR_EQUAL
			) logic_expr1 	
			| logic_expr1;
logic_expr1: logic_expr1 (AND | OR) add_expr1 | add_expr1;
add_expr1: add_expr1 ( ADD | SUB) mul_expr1 | mul_expr1;
mul_expr1: mul_expr1 (MUL | DIV | MOD) not_expr1 | not_expr1;
not_expr1: NOT not_expr1 | sign_expr1;
sign_expr1: (SUB sign_expr1) | exp91;
exp91: LB expr_while RB | operand1;
operand1:IDENTIFIER| INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT 
		| func_call| index_operators1;
expr_list1: (expr_while (COMMA expr_while)*)?;
index_operators1: IDENTIFIER LSB expr_list1 RSB;
/********************* END EXPRESSIONS ***********************/

/*********************BEGIN FRAGMENTS **********************/
fragment DIGIT: [0-9];
fragment EXPPART: [eE][+-]? [0-9]+;
fragment NonDigit: [a-zA-Z_];
fragment NonZeroDigit: [1-9];
fragment DoubleQuote: '"';
fragment ESCAPE_SEQUENCE: '\\' [bfrnt"\\];
fragment CHARLIT: ~[\b\t\f\r\n"\\] | ESCAPE_SEQUENCE;
fragment DECPART: '.' [0-9]*;
// INT_LIT: ('-'? NonZeroDigit'_'?(DIGIT'_'?)*DIGIT | '-'?DIGIT)
INT_LIT: (( NonZeroDigit DIGIT*) ('_'? DIGIT)* | '0')
	{
		self.text = self.text.replace("_","")
	};

FLOAT_LIT:( INT_LIT DECPART 
		| INT_LIT DECPART? EXPPART
		| DECPART EXPPART )
	{self.text = self.text.replace("_","")};

BOOL_LIT: TRUE | FALSE;

STRING_LIT: DoubleQuote CHARLIT* DoubleQuote
	{
		self.text = self.text[1:-1]
	}; 

array: LCB literal_element RCB;
literal_element: (literal (COMMA literal)*?)?;
literal: expr | array;
/********************* END LITERALS ***********************/

/********************* BEGIN COMMENTS ***********************/

 
/******************** SEPARATORS **********************/
LB: '(' ;
RB: ')' ;
LSB: '[';
RSB: ']';
DOT: '.';
COMMA: ',';
SEMI: ';';
COLON: ':';
LCB: '{';
RCB: '}';

/********************* KEY WORDS **********************/
AUTO: 'auto';
BREAK: 'break';
BOOLEAN: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNC: 'function';
IF: 'if';
INT: 'integer';
RETURN: 'return';
STR: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

/******************** IDENTIFIERS *********************/
IDENTIFIER: [_a-zA-Z][_a-zA-Z0-9]*;
id_arr: IDENTIFIER (LSB (INT_LIT | IDENTIFIER) (COMMA (INT_LIT | IDENTIFIER))* RSB)+;
/********************* OPERATORS **********************/
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL: '==';
NOT_EQUAL: '!=';
SMALLER: '<';
SMALLER_OR_EQUAL: '<=';
BIGGER: '>';
BIGGER_OR_EQUAL: '>=';
ASSIGN: '=';
DOUBLECOLON: '::';


/********************* END COMMENTS ***********************/


COMMENT_BLOCK: '/*' .*? '*/' -> skip;
COMMENT_LINE: '//' ~[\r\n]* -> skip;
WS : [ \t\n\r]+ -> skip ; // skip spaces, tabs, newlines
ERROR_0: ('0' DIGIT+) {raise ErrorToken('0')};
UNCLOSE_STRING: '"' CHARLIT* {self.text = self.text.replace('"','',1)};
ILLEGAL_ESCAPE: '"' CHARLIT* ('\\' ~([bfnrt\\] | '\''))
{self.text = self.text.replace('"','',1)};
ERROR_CHAR: . {raise ErrorToken(self.text)};


