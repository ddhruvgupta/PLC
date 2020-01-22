PLY Overview [from PLY documentation @ http://www.dabeaz.com/ply/ply.html#ply_nn1]

PLY consists of two separate modules; lex.py and yacc.py, both of which are found in a Python package called ply. The lex.py module is used to break input text into a collection of tokens specified by a collection of regular expression rules. yacc.py is used to recognize language syntax that has been specified in the form of a context free grammar.

Parsing Basics 

syntax is specified in terms of a BNF grammar.if you wanted to parse simple arithmetic expressions, you might first write an unambiguous grammar specification like this:

 
 expression : expression + term
            | expression - term
            | term
 
 term       : term * factor
            | term / factor
            | factor
 
 factor     : NUMBER
            | ( expression )



symbols such as NUMBER, +, -, *, and / are known as terminals and correspond to raw input tokens. 

Identifiers such as term and factor refer to grammar rules comprised of a collection of terminals and other rules. 
These identifiers are known as non-terminals.

The semantic behavior of a language is often specified using a technique known as syntax directed translation. In syntax directed translation, attributes are attached to each symbol in a given grammar rule along with an action. Whenever a particular grammar rule is recognized, the action describes what to do. For example, given the expression grammar above, you might write the specification for a simple calculator like this:

 
 Grammar                             Action
 --------------------------------    -------------------------------------------- 
 expression0 : expression1 + term    expression0.val = expression1.val + term.val
             | expression1 - term    expression0.val = expression1.val - term.val
             | term                  expression0.val = term.val
 
 term0       : term1 * factor        term0.val = term1.val * factor.val
             | term1 / factor        term0.val = term1.val / factor.val
             | factor                term0.val = factor.val
 
 factor      : NUMBER                factor.val = int(NUMBER.lexval)
             | ( expression )        factor.val = expression.val
			 
			 
			 