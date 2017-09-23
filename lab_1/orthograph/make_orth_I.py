fout=open('orth_I.txt','w')

alphabet='ΕΡΤΥΘΙΟΠΑΣΔΦΓΗΞΚΛΖΧΨΩΒΝΜ'
#alphabet='ΧΥ'
#fout.write('0 0 eps eps 0\n')
for i in alphabet:
	fout.write('0 0 '+i+' '+i+' 0\n')
fout.write('0')
