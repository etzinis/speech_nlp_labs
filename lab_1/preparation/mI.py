f = open('I.txt','w')
fal=open('alphabet.syms','w')
cost = 999
english='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in english:
	f.write('0 0 ' + i + ' ' + i + ' ' + str(cost) + '\n')
f.write('0')

stringin='eps'+ ' ' +'0'
fal.write(stringin)
fal.write('\n')
for j in range(len(english)):
	i=j+1
	stringin=english[j]+ ' ' +str(i)
	fal.write(stringin)
	fal.write('\n')


