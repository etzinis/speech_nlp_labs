all: G I A1 A2

G: Gpy G1 G2 
Gpy:
	python3 vima1.py
G1:	
	fstcompile --isymbols=inputG --osymbols=outputG G.txt G.fst
G2:	
	fstdraw --isymbols=inputG --osymbols=outputG G.fst G.dot|dot -Tps G.dot >G.ps
	fstprint --isymbols=inputG --osymbols=outputG G.fst

I: Ipy I1 I2
Ipy:
	python3 mI.py
I1:
	fstcompile --isymbols=alphabet.syms --osymbols=alphabet.syms I.txt I.fst
I2:
	fstdraw --isymbols=alphabet.syms --osymbols=alphabet.syms I.fst I.dot|dot -Tps I.dot >I.ps

A1: A1py A11 Adet Amin 
A1py:
	python3 A1.py
A11:
	fstcompile --isymbols=dict.txt --osymbols=dict.txt A1.txt A1.fst
Adet:
	fstdeterminize A1.fst >A1-det.fst
Amin:	
	fstminimize A1-det.fst min-A1.fst
Amindraw:
	fstdraw --isymbols=dict.txt --osymbols=dict.txt min-A1.fst A1.dot|dot -Tps A1.dot >A1.ps

A2: A2py A21 A2det A2min 
A2py:
	python3 A2.py
A21:
	fstcompile --isymbols=dicten.txt --osymbols=dicten.txt A2.txt A2.fst
A2det:
	fstdeterminize A2.fst >A2-det.fst
A2min:   
	fstminimize A2-det.fst min-A2.fst
A2mindraw:
	fstdraw --isymbols=dicten.txt --osymbols=dicten.txt min-A2.fst A2.dot|dot -Tps A2.dot >A2.ps
