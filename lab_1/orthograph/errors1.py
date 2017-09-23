import math
fco = open('train_co.txt', 'r')
fwr =open('train_wr.txt', 'r')
fcoal = open('train_co_al.txt', 'w')
fwral =open('train_wr_al.txt', 'w')

#first we align the two files
colines = fco.readlines()
wrlines = fwr.readlines()
for i in colines:
	cols = i.split()
	for j in cols:
		fcoal.write(j+'\n')
	
for i in wrlines:
	cols = i.split()
	for j in cols:
		fwral.write(j+'\n')

#here we check only for 1 error per word


fcoal = open('train_co_al.txt', 'r')
fwral =open('train_wr_al.txt', 'r')
coword = fcoal.readlines()
wrword = fwral.readlines()
sub=0
swap=0
deletion=0
insertion=0
total=0
for i in range(len(coword)):
	testword=wrword[i]
	rightword=coword[i]

	#CHECK FOR ONLY ONE SUBSTITUTION OR ONLY ONE SWAP BETWEEN LETTERS
	if len(coword[i])==len(wrword[i]):
		
		replaced=0
		#here we check for replacements
		for j in range(len(coword[i])):
			if (rightword[j]!=testword[j]) and (replaced==0): #then we have only one substitution
				replaced=1
			elif (rightword[j]!=testword[j]) and (replaced==1): #then we have more than one substitutions
				replaced=2
				break
			else:
				continue
		if replaced==1:
			total+=1
			sub+=1
		#--------------------------------------------

		#here we check for swaps
		allagh=0
		prevco=rightword[0]
		prevte=testword[0]
		for j in range(1,len(coword[i])):
			if (rightword[j]==prevte) and (testword[j]==prevco) and (testword[j]!=rightword[j]) and (allagh==0):
				allagh=1
				prevco=rightword[j]
				prevte=testword[j]
			elif (rightword[j]==testword[j]):
				prevco=rightword[j]
				prevte=testword[j]
				continue
			else:
				allagh=2
				break
			
		if allagh==1:
			total+=1
			swap+=1
	#--------------------------------------------
	#----------------------------------------------------------------------------------
	
	#WE CHECK FOR ONLY ONE INSERTION
	elif len(coword[i])==len(wrword[i])+1:
		ins=0
		jco=0
		jte=0	
		while jco <len(coword[i]) and jte<len(testword):
			if (rightword[jco]==testword[jte]):
				jco+=1
				jte+=1
				continue
			elif (rightword[jco]!=testword[jte]) and ins==0:
				jco+=1
				ins=1
				continue
			else:
				ins=2
				break
			
		if ins==1:
			total+=1
			insertion+=1

	#CHECK FOR ONLY ONE DELETION
	elif len(coword[i])+1==len(wrword[i]):
		de=0
		jco=0
		jte=0	
		while jco <len(coword[i]) and jte<len(testword):
			if (rightword[jco]==testword[jte]):
				jco+=1
				jte+=1
				continue
			elif (rightword[jco]!=testword[jte]) and de==0:
				jte+=1
				de=1
				continue
			else:
				de=2
				break
			
		if de==1:
			total+=1
			deletion+=1

costsub=-math.log10(sub/total)
costswap=-math.log10(swap/total)
costinsertion=-math.log10(insertion/total)
costdeletion=-math.log10(deletion/total)

print('\nCosts Computed from the training \n')	
print('substitution',str(costsub))
print('swap',str(costswap))
print('insertion',str(costinsertion))
print('deletion',str(costdeletion))
print('\n')

#HERE WE CREATE THE TRANDUCER E
fe=open('orth_E.txt','w')
#alphabet='ΧΥ'
alphabet='ΕΡΤΥΘΙΟΠΑΣΔΦΓΗΞΚΛΖΧΨΩΒΝΜ'
cnt=2
fe.write('0 1 eps eps 0'+'\n') #we can have no error at all
for i in range(len(alphabet)):
	fe.write('0 1 eps '+alphabet[i]+' '+str(costinsertion)+'\n')
	fe.write('0 1 '+alphabet[i]+' eps '+str(costdeletion)+'\n')
	for j in range(len(alphabet)):
		if alphabet[i]!=alphabet[j]:
			fe.write('0 1 '+alphabet[i]+' '+alphabet[j]+' '+str(costsub)+'\n')
	for j in range(len(alphabet)):
		if alphabet[i]!=alphabet[j]:
			fe.write('0 '+str(cnt)+' '+alphabet[i]+' '+alphabet[j]+' '+str(costswap)+'\n')
			fe.write(str(cnt)+' 1 '+alphabet[j]+' '+alphabet[i]+' '+str(0)+'\n')
			cnt+=1
fe.write(str(1))		



