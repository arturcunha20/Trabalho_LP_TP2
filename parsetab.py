
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND AS CALL CREATE DISCARD DO END FROM JOIN LIMIT LOAD PROCEDURE SAVE SELECT SHOW TABLE USING WHERE nr string var vars : S  vars : vars S S : comands\n              | procedimentos\n              | v\n              | call_procedimentos comands : LOAD table\n                    | DISCARD table\n                    | SHOW table\n                    | SAVE table\n                    | SELECT select\n                    | CREATE table  table : TABLE var ';'\n                  | TABLE var from\n                  | TABLE var as  select : '*' from\n                   | a_list from a_list : var  a_list : a_list ',' var  as : AS string ';'  v : var  from : FROM var ';'\n                 | FROM var where\n                 | FROM comands\n                 | FROM var join\n                 | FROM string ';'\n                 | FROM var limit  limit : LIMIT nr ';'  join : JOIN var using using : USING '(' var ')' ';'  where :  WHERE operadores  operadores : var '=' nr rec\n                       | var '=' string rec\n                       | var '<' '>' nr rec\n                       | var '<' '>' string rec\n                       | var '<' nr rec\n                       | var '>' nr rec\n                       | var '<' '=' nr rec\n                       | var '>' '=' nr rec rec : ';'\n                | AND operadores\n                | limit  procedimentos : PROCEDURE var DO list_com END  list_com : comands  list_com : list_com comands  call_procedimentos : CALL var ';'"
    
_lr_action_items = {'LOAD':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,50,54,55,56,57,58,65,67,76,77,79,80,83,85,88,89,90,91,92,94,],[7,7,-1,-3,-4,-5,-6,-21,-2,-7,-8,-9,-10,-11,-12,-16,7,-17,7,-46,-13,-14,-15,-24,7,-44,-22,-23,-25,-27,-26,-43,-45,-20,-31,-29,-28,-32,-40,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'DISCARD':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,50,54,55,56,57,58,65,67,76,77,79,80,83,85,88,89,90,91,92,94,],[8,8,-1,-3,-4,-5,-6,-21,-2,-7,-8,-9,-10,-11,-12,-16,8,-17,8,-46,-13,-14,-15,-24,8,-44,-22,-23,-25,-27,-26,-43,-45,-20,-31,-29,-28,-32,-40,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'SHOW':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,50,54,55,56,57,58,65,67,76,77,79,80,83,85,88,89,90,91,92,94,],[9,9,-1,-3,-4,-5,-6,-21,-2,-7,-8,-9,-10,-11,-12,-16,9,-17,9,-46,-13,-14,-15,-24,9,-44,-22,-23,-25,-27,-26,-43,-45,-20,-31,-29,-28,-32,-40,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'SAVE':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,50,54,55,56,57,58,65,67,76,77,79,80,83,85,88,89,90,91,92,94,],[10,10,-1,-3,-4,-5,-6,-21,-2,-7,-8,-9,-10,-11,-12,-16,10,-17,10,-46,-13,-14,-15,-24,10,-44,-22,-23,-25,-27,-26,-43,-45,-20,-31,-29,-28,-32,-40,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'SELECT':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,50,54,55,56,57,58,65,67,76,77,79,80,83,85,88,89,90,91,92,94,],[11,11,-1,-3,-4,-5,-6,-21,-2,-7,-8,-9,-10,-11,-12,-16,11,-17,11,-46,-13,-14,-15,-24,11,-44,-22,-23,-25,-27,-26,-43,-45,-20,-31,-29,-28,-32,-40,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'CREATE':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,31,32,34,35,36,37,38,41,44,45,47,48,49,50,54,55,56,57,58,65,67,76,77,79,80,83,85,88,89,90,91,92,94,],[12,12,-1,-3,-4,-5,-6,-21,-2,-7,-8,-9,-10,-11,-12,-16,12,-17,12,-46,-13,-14,-15,-24,12,-44,-22,-23,-25,-27,-26,-43,-45,-20,-31,-29,-28,-32,-40,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'PROCEDURE':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,32,35,36,37,38,41,47,48,49,50,54,55,57,58,65,67,76,77,79,80,83,85,88,89,90,91,92,94,],[13,13,-1,-3,-4,-5,-6,-21,-2,-7,-8,-9,-10,-11,-12,-16,-17,-46,-13,-14,-15,-24,-22,-23,-25,-27,-26,-43,-20,-31,-29,-28,-32,-40,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'var':([0,1,2,3,4,5,6,11,13,14,15,16,17,18,19,20,21,22,26,30,31,32,33,35,36,37,38,41,47,48,49,50,51,52,54,55,57,58,65,67,75,76,77,78,79,80,83,85,88,89,90,91,92,94,],[14,14,-1,-3,-4,-5,-6,25,27,-21,28,-2,-7,29,-8,-9,-10,-11,-12,-16,40,-17,43,-46,-13,-14,-15,-24,-22,-23,-25,-27,59,60,-26,-43,-20,-31,-29,-28,87,-32,-40,59,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'CALL':([0,1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,32,35,36,37,38,41,47,48,49,50,54,55,57,58,65,67,76,77,79,80,83,85,88,89,90,91,92,94,],[15,15,-1,-3,-4,-5,-6,-21,-2,-7,-8,-9,-10,-11,-12,-16,-17,-46,-13,-14,-15,-24,-22,-23,-25,-27,-26,-43,-20,-31,-29,-28,-32,-40,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'$end':([1,2,3,4,5,6,14,16,17,19,20,21,22,26,30,32,35,36,37,38,41,47,48,49,50,54,55,57,58,65,67,76,77,79,80,83,85,88,89,90,91,92,94,],[0,-1,-3,-4,-5,-6,-21,-2,-7,-8,-9,-10,-11,-12,-16,-17,-46,-13,-14,-15,-24,-22,-23,-25,-27,-26,-43,-20,-31,-29,-28,-32,-40,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'TABLE':([7,8,9,10,12,],[18,18,18,18,18,]),'*':([11,],[23,]),'END':([17,19,20,21,22,26,30,32,36,37,38,41,44,45,47,48,49,50,54,56,57,58,65,67,76,77,79,80,83,85,88,89,90,91,92,94,],[-7,-8,-9,-10,-11,-12,-16,-17,-13,-14,-15,-24,55,-44,-22,-23,-25,-27,-26,-45,-20,-31,-29,-28,-32,-40,-42,-33,-36,-37,-41,-34,-35,-38,-39,-30,]),'FROM':([23,24,25,29,43,],[31,31,-18,31,-19,]),',':([24,25,43,],[33,-18,-19,]),'DO':([27,],[34,]),';':([28,29,40,42,46,61,68,69,71,73,81,82,84,86,93,],[35,36,47,54,57,67,77,77,77,77,77,77,77,77,94,]),'AS':([29,],[39,]),'string':([31,39,62,70,],[42,46,69,82,]),'WHERE':([40,],[51,]),'JOIN':([40,],[52,]),'LIMIT':([40,68,69,71,73,81,82,84,86,],[53,53,53,53,53,53,53,53,53,]),'nr':([53,62,63,64,70,72,74,],[61,68,71,73,81,84,86,]),'=':([59,63,64,],[62,72,74,]),'<':([59,],[63,]),'>':([59,63,],[64,70,]),'USING':([60,],[66,]),'(':([66,],[75,]),'AND':([68,69,71,73,81,82,84,86,],[78,78,78,78,78,78,78,78,]),')':([87,],[93,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'vars':([0,],[1,]),'S':([0,1,],[2,16,]),'comands':([0,1,31,34,44,],[3,3,41,45,56,]),'procedimentos':([0,1,],[4,4,]),'v':([0,1,],[5,5,]),'call_procedimentos':([0,1,],[6,6,]),'table':([7,8,9,10,12,],[17,19,20,21,26,]),'select':([11,],[22,]),'a_list':([11,],[24,]),'from':([23,24,29,],[30,32,37,]),'as':([29,],[38,]),'list_com':([34,],[44,]),'where':([40,],[48,]),'join':([40,],[49,]),'limit':([40,68,69,71,73,81,82,84,86,],[50,79,79,79,79,79,79,79,79,]),'operadores':([51,78,],[58,88,]),'using':([60,],[65,]),'rec':([68,69,71,73,81,82,84,86,],[76,80,83,85,89,90,91,92,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> vars","S'",1,None,None,None),
  ('vars -> S','vars',1,'p_varias00','logic_grammar.py',22),
  ('vars -> vars S','vars',2,'p_varias01','logic_grammar.py',26),
  ('S -> comands','S',1,'p_S','logic_grammar.py',31),
  ('S -> procedimentos','S',1,'p_S','logic_grammar.py',32),
  ('S -> v','S',1,'p_S','logic_grammar.py',33),
  ('S -> call_procedimentos','S',1,'p_S','logic_grammar.py',34),
  ('comands -> LOAD table','comands',2,'p_comands','logic_grammar.py',38),
  ('comands -> DISCARD table','comands',2,'p_comands','logic_grammar.py',39),
  ('comands -> SHOW table','comands',2,'p_comands','logic_grammar.py',40),
  ('comands -> SAVE table','comands',2,'p_comands','logic_grammar.py',41),
  ('comands -> SELECT select','comands',2,'p_comands','logic_grammar.py',42),
  ('comands -> CREATE table','comands',2,'p_comands','logic_grammar.py',43),
  ('table -> TABLE var ;','table',3,'p_table','logic_grammar.py',47),
  ('table -> TABLE var from','table',3,'p_table','logic_grammar.py',48),
  ('table -> TABLE var as','table',3,'p_table','logic_grammar.py',49),
  ('select -> * from','select',2,'p_select','logic_grammar.py',56),
  ('select -> a_list from','select',2,'p_select','logic_grammar.py',57),
  ('a_list -> var','a_list',1,'p_aList00','logic_grammar.py',62),
  ('a_list -> a_list , var','a_list',3,'p_aList01','logic_grammar.py',66),
  ('as -> AS string ;','as',3,'p_as','logic_grammar.py',71),
  ('v -> var','v',1,'p_var','logic_grammar.py',75),
  ('from -> FROM var ;','from',3,'p_from','logic_grammar.py',79),
  ('from -> FROM var where','from',3,'p_from','logic_grammar.py',80),
  ('from -> FROM comands','from',2,'p_from','logic_grammar.py',81),
  ('from -> FROM var join','from',3,'p_from','logic_grammar.py',82),
  ('from -> FROM string ;','from',3,'p_from','logic_grammar.py',83),
  ('from -> FROM var limit','from',3,'p_from','logic_grammar.py',84),
  ('limit -> LIMIT nr ;','limit',3,'p_limit','logic_grammar.py',92),
  ('join -> JOIN var using','join',3,'p_join','logic_grammar.py',96),
  ('using -> USING ( var ) ;','using',5,'p_using','logic_grammar.py',100),
  ('where -> WHERE operadores','where',2,'p_where','logic_grammar.py',104),
  ('operadores -> var = nr rec','operadores',4,'p_operadores00','logic_grammar.py',108),
  ('operadores -> var = string rec','operadores',4,'p_operadores00','logic_grammar.py',109),
  ('operadores -> var < > nr rec','operadores',5,'p_operadores00','logic_grammar.py',110),
  ('operadores -> var < > string rec','operadores',5,'p_operadores00','logic_grammar.py',111),
  ('operadores -> var < nr rec','operadores',4,'p_operadores00','logic_grammar.py',112),
  ('operadores -> var > nr rec','operadores',4,'p_operadores00','logic_grammar.py',113),
  ('operadores -> var < = nr rec','operadores',5,'p_operadores00','logic_grammar.py',114),
  ('operadores -> var > = nr rec','operadores',5,'p_operadores00','logic_grammar.py',115),
  ('rec -> ;','rec',1,'p_operadores01','logic_grammar.py',123),
  ('rec -> AND operadores','rec',2,'p_operadores01','logic_grammar.py',124),
  ('rec -> limit','rec',1,'p_operadores01','logic_grammar.py',125),
  ('procedimentos -> PROCEDURE var DO list_com END','procedimentos',5,'p_procedimentos00','logic_grammar.py',135),
  ('list_com -> comands','list_com',1,'p_procedimentos01','logic_grammar.py',139),
  ('list_com -> list_com comands','list_com',2,'p_procedimentos02','logic_grammar.py',143),
  ('call_procedimentos -> CALL var ;','call_procedimentos',3,'p_callProcedimentos','logic_grammar.py',148),
]
