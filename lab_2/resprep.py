f = open('results.txt')
lines = f.readlines()
n=0
ssub=0
sins=0
sd=0
sscore=0
for line in lines:
	cols = line.split()
	if(len(cols)>1):
		if cols[0]=='%WER':
			WER=cols[1]
			sscore+=float(WER)
			n+=1

	for i in range(len(cols)-1,0,-1):
		if(cols[i]=='sub'):
			sub=float(cols[i-1])
			ssub+=sub
		if(cols[i]=='del,'):
			d=float(cols[i-1])
			sd+=d
		if(cols[i]=='ins,'):
			ins=float(cols[i-1])
			sins+=ins
print('AVERAGE VALUES OF OUR MODEL FOR THE TEST DATA\n')
print('AVERAGE INS: '+str(sins/n))	
print('AVERAGE DEL: '+str(sd/n))		
print('AVERAGE SUB: '+str(ssub/n))		
print('AVERAGE WER: '+str(sscore/n))			

f.close()
