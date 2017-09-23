import sys
import os
fco = open('test_co.txt', 'r')
fwr =open('test_wr.txt', 'r')
fcoal = open('test_co_al.txt', 'w')
fwral =open('test_wr_al.txt', 'w')

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
fcoal.close()
fwral.close()
fco.close()
fwr.close()
#-----------------------------------------------

#then we create the fst file for every acceptor for wr words
fcoal = open('test_co_al.txt', 'r')
fwral =open('test_wr_al.txt', 'r')
fres1=open('Result1', 'w')
fres2=open('Result2', 'w')


#Make the dictionary-----------------------------------

fio=open('io','r')
lines=fio.readlines()
dict=[0 for x in range(len(lines))]
for line in lines:
	cols = line.split()
	dict[int(cols[1])]=cols[0]
fio.close()

#--------------------------------------------------------

coword = fcoal.readlines()
wrword = fwral.readlines()
fcoal.close()
fwral.close()
#we pre compile the 5th step of lab preparation in order to just compose only the needmost part
os.system("make prepareA1")
cnt=0
total1=len(wrword)-1
for word in wrword:
	colw=word.split()
	colc=coword[cnt].split()
	#after that we truncate this file in order to make the other acceptors in the same file
	facc=open('orth_acc.txt', 'w')
	state=0
	for letter in word:
		if letter!='\n':
			facc.write(str(state)+' '+str(state+1)+' '+letter+' '+letter+'\n')
			state+=1
	facc.write(str(state)+'\n')
	facc.close()
	#we use the fst tool in order to create the acceptor for every word 

	os.system("make -s one_word")
	os.system("make -s one_word2")

	#after that we write the result in a file in order to compare the best words for every model S1, S2
	fshort=open('Shortest', 'r')
	lines=fshort.readlines()
	temp=[]
	for i in range(2,len(lines)):
		cols = lines[i].split()
		if len(cols)>3:
			temp.append(cols[3])
	if len(lines)>1:	
		cols = lines[0].split()
		if len(cols)>3:
			temp.append(cols[3])
		temp.reverse()

	#Now we have in temp the produced word and we have to cross check it with the dictionary from io
	
	for j in temp:
		if int(j)!=0:
			fres1.write(dict[int(j)])
	fshort.close()
	fres1.write(' '+colw[0]+' '+colc[0]+'\n')
	#we write the words in each result file like this: \word from orthograph\ \wrong word\ \right word\


	#Now the same for S2 -------------------------------------------------------------------------

	fshort=open('Shortest2', 'r')
	lines=fshort.readlines()
	temp=[]
	for i in range(2,len(lines)):
		cols = lines[i].split()
		if len(cols)>3:
			temp.append(cols[3])
	if len(lines)>1:	
		cols = lines[0].split()
		if len(cols)>3:
			temp.append(cols[3])
		temp.reverse()

	#Now we have in temp the produced word and we have to cross check it with the dictionary from io
	
	for j in temp:
		if int(j)!=0:
			fres2.write(dict[int(j)])
	fshort.close()
	fres2.write(' '+colw[0]+' '+colc[0]+'\n')

	#---------------------------------------------------------------------------------------------
	print('\n\nLOADING '+str(cnt)+'/'+str(total1)+'\n\n')
	cnt+=1
fres1.close()
fres2.close()


#Here we canmeasure the correctness of WS1A1 machine
nochangewords=0
correctedwords=0
wrongwords=0
cantmatch=0
fres1=open('Result1', 'r')
words=fres1.readlines()
for word in words:
	cols=word.split()
	if len(cols)>=3:
		if cols[0]==cols[1]==cols[2]:
			nochangewords+=1
		elif cols[1]!=cols[2] and cols[0]==cols[2]:
			correctedwords+=1
		else:
			wrongwords+=1
	else:
		cantmatch+=1
print('\nMODEL WS1A1\n')
print('No Change Words '+str(nochangewords))
print('Corrected Words '+str(correctedwords))
print('Wrong Words '+str(wrongwords))
print('Model 1 Could not match '+ str(cantmatch))
percentage=round((correctedwords/(wrongwords+cantmatch))*100,2)
print('\nModel 1 Correct Ratio=(Corrected Words+No Change Words)/(Total)='+ str(percentage)+'%')
fres1.close()

#Here we canmeasure the correctness of WS2A1 machine
nochangewords=0
correctedwords=0
wrongwords=0
cantmatch=0
fres2=open('Result2', 'r')
words=fres2.readlines()
for word in words:
	cols=word.split()
	if len(cols)>=3:
		if cols[0]==cols[1]==cols[2]:
			nochangewords+=1
		elif cols[1]!=cols[2] and cols[0]==cols[2]:
			correctedwords+=1
		else:
			wrongwords+=1
	else:
		cantmatch+=1
print('\nMODEL WS2A1\n')
print('No Change Words '+str(nochangewords))
print('Corrected Words '+str(correctedwords))
print('Wrong Words '+str(wrongwords))
print('Model 2 Could not match '+ str(cantmatch))
percentage=round((correctedwords/(wrongwords+cantmatch))*100,2)
print('\nModel 2 Correct Ratio=(Corrected Words+No Change Words)/(Total)='+ str(percentage)+'%')

fres2.close()


