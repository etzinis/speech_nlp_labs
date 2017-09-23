import sys

word0='' 
word1=''
dictionary={}
dictionary2={}
dictionary3={}
dictionary_rules1={}
dictionary_rules2={}
dictionary_final1={}
dictionary_final2={}
dictionary_final3={}
i=0	    
if len(sys.argv)==3:
    f0=open(sys.argv[1],'r')
    f1=open(sys.argv[2],'r')
else:
    f0=open('train_greng.txt','r')
    f1=open('train_gr.txt','r')
a0=f0.read(1)
a1=f1.read(1)
while a0!='' and a1!='':
    while a0=='\n':
        a0=f0.read(1)
    while a1=='\n':
        a1=f1.read(1)
    while a0!=' ' and a0!='' and a0!='\n': 
        word0+=a0
        a0=f0.read(1)
    while a1!=' ' and a1!='' and a1!='\n': 
        word1+=a1
        a1=f1.read(1)
    if len(word0)==len(word1) and a0!='' and a1!='':
        for i in range(0,len(word0)):
            if not word0[i] in dictionary:
                dictionary[word0[i]]=[word1[i]] 
            elif not word1[i] in dictionary[word0[i]]:
                dictionary[word0[i]].append(word1[i])
            try:
                dictionary_rules1[word0[i]+word1[i]]+=1
            except:
                dictionary_rules1[word0[i]+word1[i]]=1
            
    elif len(word0)>len(word1)>0:
        times=len(word0)-len(word1)
        k=0
        j=0
        while i<len(word0) and k<times and j<len(word1):
            if i<len(word0)-1:    
                temp=word0[i]+word0[i+1]
            else:
                temp=word0[i]
            try:
                word1[j]
            except:
                print(word1,word0,j,i)
                print(dictionary)
                print(dictionary2)
            if (not word0[i] in dictionary) or (not word1[j] in dictionary[word0[i]]):
                if (not temp in dictionary2) and len(temp)>1:           
                    try:
                        dictionary2[temp]=[word1[j]]
                    except:
                        print(word0,word1,j) 
                    try:
                        dictionary_rules1[temp+word1[j]]+=1
                    except:
                        dictionary_rules1[temp+word1[j]]=1
                    i+=2
                    j+=1
                    k+=1
                elif len(temp)==1:
                    try:
                        dictionary_rules1[temp+word1[j]]+=1
                    except:
                        dictionary_rules1[temp+word1[j]]=1
                    if not temp in dictionary:
                        dictionary[temp]=[word1[j]] 
                    elif not word1[j] in dictionary[temp]:
                        dictionary[temp].append(word1[j])
                    i+=1
                    j+=1
                elif not word1[j] in dictionary2[temp]:
                    dictionary2[temp].append(word1[j])
                    try:
                        dictionary_rules1[temp+word1[j]]+=1
                    except:
                        dictionary_rules1[temp+word1[j]]=1                                       
                    i=i+2
                    j+=1
                    k+=1
                else:
                    try:
                        dictionary_rules1[temp+word1[j]]+=1
                    except:
                        dictionary_rules1[temp+word1[j]]=1
                    i+=2
                    j+=1
                    k+=1
            elif word0[i] in dictionary:
                if not word1[j] in dictionary[word0[i]]:
                    dictionary[word0[i]].append(word1[j])
                try:
                    dictionary_rules1[word0[i]+word1[j]]+=1
                except:
                    dictionary_rules1[word0[i]+word1[j]]=1
                i=i+1
                j+=1
            else:
                dictionary[word0[i]]=[word1[j]]
                try:
                    dictionary_rules1[word0[i]+word1[j]]+=1
                except:
                    dictionary_rules1[word0[i]+word1[j]]=1
                i+=1
                j+=1
        while j<len(word1) and i<len(word0):
            if not word0[i] in dictionary:
                dictionary[word0[i]]=[word1[j]] 
            elif not word1[j] in dictionary[word0[i]]:
                dictionary[word0[i]].append(word1[j])     
            try:
                dictionary_rules1[word0[i]+word1[j]]+=1
            except:
                dictionary_rules1[word0[i]+word1[j]]=1 
            j=j+1
            i=i+1 
    elif len(word1)>len(word0)>0:
        times=len(word1)-len(word0)
        k=0
        j=0
        while j<len(word1) and k<times:
            if j<len(word1)-1:    
               temp=word1[j]+word1[j+1]
            else:
                temp=word1[j]
            if (not word0[i] in dictionary) or (not word1[j] in dictionary[word0[i]]):
                if ((word0[i] in dictionary3)and(not temp in dictionary3[word0[i]])or (not word0[i] in dictionary3))  and len(temp)>1:   
                    try:
                        dictionary3[word0[i]].append(temp) 
                    except:
                        dictionary3[word0[i]]=[temp]
                    try:
                        dictionary_rules2[word0[i]+temp]+=1
                    except:
                        dictionary_rules2[word0[i]+temp]=1 
                    i+=1
                    j+=2
                    k+=1
                elif len(temp)==1:
                    try:
                        dictionary_rules1[word0[i]+temp]+=1
                    except:
                        dictionary_rules1[word0[i]+temp]=1
                    if not word0[i] in dictionary:
                        dictionary[word0[i]]=[temp] 
                    elif not temp in dictionary[word0[i]]:
                        dictionary[word0[i]].append(temp)
                    j+=1
                    i+=1
                else:
                    try:
                       dictionary_rules2[word0[i]+temp]+=1
                    except:
                       dictionary_rules2[word0[i]+temp]=1
                    j+=2
                    i+=1
            elif word0[i] in dictionary:
                if not word1[j] in dictionary[word0[i]]:
                    dictionary[word0[i]].append(word1[j])
                try:
                    dictionary_rules1[word0[i]+word1[j]]+=1
                except:
                    dictionary_rules1[word0[i]+word1[j]]=1  
                i=i+1
                j+=1
            else:
                dictionary[word0[i]]=[word1[j]]
                try:
                   dictionary_rules1[word0[i]+word1[j]]+=1
                except:
                   dictionary_rules1[word0[i]+word1[j]]=1 
                i+=1
                j+=1   
        while j<len(word1) and i<len(word0):
            if not word0[i] in dictionary:
                dictionary[word0[i]]=[word1[j]] 
            elif not word1[j] in dictionary[word0[i]]:
                dictionary[word0[i]].append(word1[j])     
            try:
                dictionary_rules1[word0[i]+word1[j]]+=1
            except:
                dictionary_rules1[word0[i]+word1[j]]=1
            j=j+1
            i=i+1       


    word0=''
    word1=''
    a0=f0.read(1)
    a1=f1.read(1)
    i=0

rulecount=0
for i in dictionary_rules1:
    rulecount+=dictionary_rules1[i]
for i in dictionary_rules2:
    rulecount+=dictionary_rules2[i]
for i in dictionary_rules1:
    dictionary_rules1[i]/=rulecount
for i in dictionary_rules2:
    dictionary_rules2[i]/=rulecount

for rule in dictionary_rules1:
    if (not (rule[0]==rule[1] and len(rule)==2)) and dictionary_rules1[rule]>0.0003:
        if len(rule)==2:
            dictionary_final1[rule]=dictionary_rules1[rule]
            print("o kanonas {} se {} emfanizetai me pithanothta  {}".format(rule[0],rule[1],dictionary_rules1[rule]))
        elif dictionary_rules1[rule]>0.0007: 
           dictionary_final2[rule]=dictionary_rules1[rule]
           print("o kanonas {} se {} emfanizetai me pithanothta  {}".format(rule[0:2],rule[2:],dictionary_rules1[rule]))
            
for rule in dictionary_rules2:       
    dictionary_final3[rule]=dictionary_rules2[rule]
    print("o kanonas {} se {} emfanizetai me pithanothta  {}".format(rule[0],rule[1:],dictionary_rules2[rule])) 



#print (dictionary_final1)
#print (dictionary_final2)
#print (dictionary_final3)
print ("to sunolo twn kanonwn einai {}!".format(len(dictionary_final1)+len(dictionary_final2)+len(dictionary_final3)))


fin = open('inputG', 'w')
fout= open('outputG', 'w')
fG = open('G.txt', 'w')

#for the fst file
for rule in dictionary_final1:
	string='0 0 '+rule[0]+ ' ' +rule[1]+ ' ' +str(dictionary_final1[rule])
	fG.write(string)
	fG.write('\n')
for rule in dictionary_final2:
	string='0 0 '+rule[0:2]+ ' ' +rule[2:]+ ' ' +str(dictionary_final2[rule])
	fG.write(string)
	fG.write('\n')
for rule in dictionary_final3:
	string='0 0 '+rule[0]+ ' ' +rule[1:]+ ' ' +str(dictionary_final3[rule])
	fG.write(string)
	fG.write('\n')
fG.write ('0')

#for the input
stringin='<epsilon>'+ ' ' +'0'
fin.write(stringin)
fin.write('\n')
#for the output
stringout='<epsilon>'+ ' ' +'0'
fout.write(stringout)
fout.write('\n')
l=0
for rule in dictionary_final1:
	l+=1
	stringin=rule[0]+ ' ' +str(l)
	fin.write(stringin)
	fin.write('\n')
	stringout=rule[1]+ ' ' +str(l)
	fout.write(stringout)
	fout.write('\n')
for rule in dictionary_final2:
	l+=1
	stringin=rule[0:2]+ ' ' +str(l)
	fin.write(stringin)
	fin.write('\n')
	stringout=rule[2:]+ ' ' +str(l)
	fout.write(stringout)
	fout.write('\n')
for rule in dictionary_final3:
	l+=1
	stringin=rule[0]+ ' ' +str(l)
	fin.write(stringin)
	fin.write('\n')
	stringout=rule[1:]+ ' ' +str(l)
	fout.write(stringout)
	fout.write('\n')




