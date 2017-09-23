import sys
fdict = open('en_caps_noaccent.dict', 'r')
fA2 = open('A2.txt' , 'w')
fdic = open('dicten.txt' , 'w')
lines = fdict.readlines()
dirline=0
finals=[]
for curline in lines:
    if (dirline!=0):
        i=0
        fA2.write('0 '+str(dirline)+' '+curline[i]+' '+curline[i]+'\n')
        dirline+=1
        for i in range(1,len(curline)-1):
            fA2.write(str(dirline-1)+' '+str(dirline)+' '+curline[i]+' '+curline[i]+'\n')
            dirline+=1
        finals.append(dirline-1)
    else:
        dirline+=1	
for j in finals:
    fA2.write(str(j)+'\n')

english='QWERTYUIOPASDFGHJKLZXCVBNM'
for j in range(len(english)):
    fdic.write(english[j]+' '+str(j)+'\n')
