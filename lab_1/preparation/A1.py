import sys
fdict = open('el_caps_noaccent.dict', 'r')
fA1 = open('A1.txt' , 'w')
fdic = open('dict.txt' , 'w')
lines = fdict.readlines()
dirline=0
finals=[]
for curline in lines:
    if (dirline!=0):
        i=0
        fA1.write('0 '+str(dirline)+' '+curline[i]+' '+curline[i]+'\n')
        dirline+=1
        for i in range(1,len(curline)-1):
            fA1.write(str(dirline-1)+' '+str(dirline)+' '+curline[i]+' '+curline[i]+'\n')
            dirline+=1
        finals.append(dirline-1)
    else:
        dirline+=1	
for j in finals:
    fA1.write(str(j)+'\n')

greek='ΕΡΤΥΘΙΟΠΑΣΔΦΓΗΞΚΛΖΧΨΩΒΝΜ'
for j in range(len(greek)):
    fdic.write(greek[j]+' '+str(j)+'\n')
    
    
