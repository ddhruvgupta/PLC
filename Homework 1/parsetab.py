
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIV ID IF LBRACE MINUS NUMBER PLUS RBRACE SEMI TIMES WITHwaeStart : wae SEMIwae : NUMBERwae : IDwae : LBRACE PLUS wae wae RBRACEwae : LBRACE MINUS wae wae RBRACEwae : LBRACE TIMES wae wae RBRACEwae : LBRACE DIV wae wae RBRACEwae : LBRACE IF wae wae wae RBRACEwae : LBRACE WITH wae wae RBRACEwae : LBRACE ID NUMBER RBRACEwae : LBRACE ID wae RBRACE'
    
_lr_action_items = {'NUMBER':([0,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,26,28,29,30,31,32,33,35,36,],[3,-2,-3,3,3,3,3,3,3,20,3,3,3,3,3,3,3,-10,-11,-4,-5,-6,-7,-9,-8,]),'ID':([0,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,26,28,29,30,31,32,33,35,36,],[4,-2,-3,13,4,4,4,4,4,4,4,4,4,4,4,4,4,4,-10,-11,-4,-5,-6,-7,-9,-8,]),'LBRACE':([0,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,26,28,29,30,31,32,33,35,36,],[5,-2,-3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-10,-11,-4,-5,-6,-7,-9,-8,]),'$end':([1,6,],[0,-1,]),'SEMI':([2,3,4,28,29,30,31,32,33,35,36,],[6,-2,-3,-10,-11,-4,-5,-6,-7,-9,-8,]),'RBRACE':([3,4,20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,],[-2,-3,28,29,30,31,32,33,35,-10,-11,-4,-5,-6,-7,36,-9,-8,]),'PLUS':([5,],[7,]),'MINUS':([5,],[8,]),'TIMES':([5,],[9,]),'DIV':([5,],[10,]),'IF':([5,],[11,]),'WITH':([5,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'waeStart':([0,],[1,]),'wae':([0,7,8,9,10,11,12,13,14,15,16,17,18,19,26,],[2,14,15,16,17,18,19,21,22,23,24,25,26,27,34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> waeStart","S'",1,None,None,None),
  ('waeStart -> wae SEMI','waeStart',2,'p_waeStart','WAEParser.py',9),
  ('wae -> NUMBER','wae',1,'p_wae_1','WAEParser.py',14),
  ('wae -> ID','wae',1,'p_wae_2','WAEParser.py',19),
  ('wae -> LBRACE PLUS wae wae RBRACE','wae',5,'p_wae_3','WAEParser.py',24),
  ('wae -> LBRACE MINUS wae wae RBRACE','wae',5,'p_wae_4','WAEParser.py',29),
  ('wae -> LBRACE TIMES wae wae RBRACE','wae',5,'p_wae_5','WAEParser.py',34),
  ('wae -> LBRACE DIV wae wae RBRACE','wae',5,'p_wae_6','WAEParser.py',39),
  ('wae -> LBRACE IF wae wae wae RBRACE','wae',6,'p_wae_7','WAEParser.py',44),
  ('wae -> LBRACE WITH wae wae RBRACE','wae',5,'p_wae_8','WAEParser.py',49),
  ('wae -> LBRACE ID NUMBER RBRACE','wae',4,'p_wae_9','WAEParser.py',54),
  ('wae -> LBRACE ID wae RBRACE','wae',4,'p_wae_10','WAEParser.py',60),
]
