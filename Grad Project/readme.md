Write a LAMBDA Calculus Interpreter in Python/PLY using the following grammar:

Grammar:

expr : 
    NUMBER
  | NAME
  | LPAREN expr expr RPAREN
  | LPAREN LAMBDA NAME expr RPAREN
  | LPAREN OP expr expr RPAREN

Lexer Specs:

NUMBER = r’[0-9]+’
LPAREN = r’('
RPAREN = r’)'
OP = r’+|-|*|/‘
LAMBDA = r’[Ll][Aa][Mm][Bb][Dd][Aa]’
NAME = r‘[a-zA-z][a-zA-z0-9]*’
Here is a sample run of the interpreter (The output contains expressions after each beta-reduction):
[raj@tinman ~]$ python3 Lambda.py
LAMBDA> ((lambda x (* x x)) 4);
( ( lambda X ( * X X ) ) 4.0 ) 
( * 4.0 4.0 ) 
16.0 
LAMBDA> ((( (lambda x (lambda y (lambda z (* (x z) (y z))))) (lambda x (* x x)))(lambda x (+ x x))) 5);
( ( ( ( lambda X ( lambda Y ( lambda Z ( * ( X Z ) ( Y Z ) ) ) ) ) ( lambda X ( * X X ) ) ) ( lambda X ( + X X ) ) ) 5.0 ) 
( ( ( lambda Y ( lambda Z ( * ( ( lambda X ( * X X ) ) Z ) ( Y Z ) ) ) ) ( lambda X ( + X X ) ) ) 5.0 ) 
( ( ( lambda Y ( lambda Z ( * ( * Z Z ) ( Y Z ) ) ) ) ( lambda X ( + X X ) ) ) 5.0 ) 
( ( lambda Z ( * ( * Z Z ) ( ( lambda X ( + X X ) ) Z ) ) ) 5.0 ) 
( ( lambda Z ( * ( * Z Z ) ( + Z Z ) ) ) 5.0 ) 
( * ( * 5.0 5.0 ) ( + 5.0 5.0 ) ) 
250.0 
LAMBDA> exit;
[raj@tinman ~]$ 
Try to get the free-variable calculation, alpha-reduction and substitutions working at least to get most credit for the project.
Here is the rubric for the grad project

Lexer: 15 points
Parser+Data Structure Construction: 15 points
Free Variable calculation: 15 points
Alpha-conversion: 15 points
Substitution: 15 points
Evaluate Expression: 25 points

for a total of 100 points.

Try to get the first 5 parts done, at least. To test these individual parts, I have extended the grammar as follows:

exprStart : expr SEMI
exprStart : expr LBRACKET NAME EQUALS expr RBRACKET SEMI
exprStart : FV LBRACKET expr RBRACKET SEMI
exprStart : ALPHA LBRACKET expr COMMA NAME RBRACKET SEMI

expr : NUMBER
expr : NAME
expr : LPAREN expr expr RPAREN
expr : LPAREN LAMBDA NAME expr RPAREN
expr : LPAREN OP expr expr RPAREN

We have a few new tokens: LBRACKET, RBRACKET, EQUALS, FV (matches fv), ALPHA (alpha), COMMA

exprStart : expr LBRACKET NAME EQUALS expr RBRACKET SEMI
will be used for checking substitutions

exprStart : FV LBRACKET expr RBRACKET SEMI
will be used for checking free variables

exprStart : ALPHA LBRACKET expr COMMA NAME RBRACKET SEMI
will be used to check for alpha conversion

Here is a sample run (showing free-variables, alpha-convert, and substitutions):

macbook-pro:gradProject raj$ python3 Lambda.py
LAMBDA> fv[(lambda x (x y))];
Free variables:  {'Y'}
LAMBDA> alpha[(lambda x (x y)),z];
(LAMBDA Z (Z Y))
LAMBDA> (lambda x (x y))[y = (u v)];
(LAMBDA X (X (U V)))
LAMBDA> exit;