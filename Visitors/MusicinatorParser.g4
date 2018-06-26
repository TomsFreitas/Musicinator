parser grammar MusicinatorParser;

options {tokenVocab = MusicinatorLexer;}

main:	instructions* EOF ;

// "high level" definitions - statements
instructions
		: assignment
		| play
		| forStat
		| ifStat
		;

assignment
		: types (OPEN_SB CLOSE_SB)? WORD EQUAL expr SEMICOLON
		;

play 	: PLAY expr SEQUENTIALLY? (expr TIMES)? SEMICOLON 			#simplePlay
		| (AT expr | AFTER variable ALWAYS?) play					#timedPlay
		| LOOP performance												#loopPlay
		;

forStat	: FOR types WORD IN WORD OPEN_BR instructions* CLOSE_BR
		;

ifStat	: IF condition 
		  OPEN_BR  instructions* CLOSE_BR 
		  (ELIF condition OPEN_BR  instructions* CLOSE_BR)* 
		  (ELSE OPEN_BR  instructions* CLOSE_BR)?
		;


// "lower level" definitions - types, expressions and conditions
expr 	: variable 									#varExpr
		| performance 								#perExpr
		| sequence 									#seqExpr
		| number 									#numExpr
		| OPEN_PR expr CLOSE_PR						#parensExpr

		| e1=expr op=(MUL|DIV) e2=expr				#mulDivExpr
		| e1=expr op=(ADD|SUB) e2=expr				#addSubExpr

		| OPEN_SB (expr (COMMA expr)*)? CLOSE_SB 	#bracketArray
		| expr (AND expr)+							#andArray
		| e1=expr ARROW e2=expr 					#numRangeArray
		;
		

sequence
		: OPEN_SB sequence* CLOSE_SB 			#seqList
		| SOUND									#seqNote
		| CHORD									#seqChord	
		;

performance
		: (sequence|seq=variable) ON inst=variable 	#perFromSeq
		;

number 	: BAR variable BAR 						#numDuration
		| DOUBLE 								#numDouble
		| INT 									#numInt
		| GETINT OPEN_PR STRING? CLOSE_PR 		#numGetInt
		;

variable
		: WORD OPEN_SB INT CLOSE_SB
		| WORD 										
		;

types 	: SQ_LIT 
		| PF_LIT 
		| NUM_LIT
		| INST_LIT
		;

condition
		: number op=(BIGR|BIGE|SMLR|SMLE|EQLS|DIFS) number
		;
