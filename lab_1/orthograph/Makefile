orthograph: orth_training orth_I orth_E S1 S2 orth_testing

orth_training:
	python3 errors1.py

orth_I:
	python3 make_orth_I.py
	fstcompile --isymbols=io --osymbols=io orth_I.txt orth_I.fst
	fstdraw --isymbols=io --osymbols=io orth_I.fst orth_I.dot

orth_E: 
	fstcompile --isymbols=io --osymbols=io orth_E.txt orth_E.fst
	fstdraw --isymbols=io --osymbols=io orth_E.fst orth_E.dot

S1:
	fstdraw --isymbols=io --osymbols=io orth_I.fst orth_I.dot
	fstconcat orth_I.fst orth_E.fst S1.fst
	fstconcat S1.fst orth_I.fst S1.fst
	fstdraw --isymbols=io --osymbols=io S1.fst S1.dot|dot -Tps S1.dot >S1.ps

S2:
	fstconcat S1.fst S1.fst S2.fst
	fstdraw --isymbols=io --osymbols=io S2.fst S2.dot

orth_testing: 
	python3 orth_test.py

prepareA1:
	fstdeterminize A1.fst A1.fst
	fstminimize A1.fst A1.fst
	fstarcsort A1.fst A1.fst

one_word:
	fstcompile --isymbols=io --osymbols=io orth_acc.txt orth_acc.fst
	fstdraw --isymbols=io --osymbols=io orth_acc.fst orth_acc.dot
	fstcompose orth_acc.fst S1.fst WS1.fst
	fstdraw --isymbols=io --osymbols=io WS1.fst WS1.dot
	fstarcsort --sort_type=olabel WS1.fst WS1.fst
	fstcompose WS1.fst A1.fst WS1A1.fst
	fstrmepsilon WS1A1.fst WS1A1.fst
	fstdraw --isymbols=io --osymbols=io WS1A1.fst WS1A1.dot
	fstshortestpath WS1A1.fst WS1A1shortest.fst
	fstrmepsilon WS1A1shortest.fst WS1A1shortest.fst
	fstarcsort WS1A1shortest.fst WS1A1shortest.fst
	fstprint WS1A1shortest.fst >Shortest
	fstdraw --isymbols=io --osymbols=io WS1A1shortest.fst WS1A1shortest.dot

one_word2:
	fstcompile --isymbols=io --osymbols=io orth_acc.txt orth_acc.fst
	fstdraw --isymbols=io --osymbols=io orth_acc.fst orth_acc.dot
	fstcompose orth_acc.fst S2.fst WS2.fst
	fstdraw --isymbols=io --osymbols=io WS2.fst WS2.dot
	fstarcsort --sort_type=olabel WS2.fst WS2.fst
	fstcompose WS2.fst A1.fst WS2A1.fst
	fstrmepsilon WS2A1.fst WS2A1.fst
	fstdraw --isymbols=io --osymbols=io WS2A1.fst WS2A1.dot
	fstshortestpath WS2A1.fst WS2A1shortest.fst
	fstrmepsilon WS2A1shortest.fst WS2A1shortest.fst
	fstarcsort WS2A1shortest.fst WS2A1shortest.fst
	fstprint WS2A1shortest.fst >Shortest2
	fstdraw --isymbols=io --osymbols=io WS2A1shortest.fst WS21shortest.dot
