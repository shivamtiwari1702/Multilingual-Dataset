import codecs
import string


def detect_language(character):
    maxchar = max(character)
    if u'\u0900' <= maxchar <= u'\u097f' or 0<=ord(maxchar)<=127:
        return True
    else:
        return False


readData=[]
f0 = codecs.open('out.csv','r',encoding='utf-8')
templist=f0.readlines()
tempstr=''

for item in templist:
           if(detect_language(item[1])):
                tempstr+=item
f0.close()

f01 = codecs.open('out1.csv','w',encoding='utf-8')
f01.write(tempstr)
f01.close()
            
f1 = codecs.open('out1.csv','r',encoding='utf-8')
readData = f1.readlines()

for i1 in readData:
    words1 = i1.split(',')

    if words1[1]=='NA':
        fgh = words1[0]
        total=0
        freq=0
        
        for i2 in readData:
            words2=i2.split(',')
            if words2[0]==fgh and words2[1]!='NA':
                freq+=1
                total+=int(words2[1])
        words1[1]=str(int(total/freq))

        final = ','.join(words1)
        readData[readData.index(i1)]=final

    if words1[2]=='NA':
        fgh = words1[0]
        total=0
        freq=0
        
        for i2 in readData:
            words2=i2.split(',')
            if words2[0]==fgh and words2[2]!='NA':
                freq+=1
                total+=int(words2[2])
        words1[2]=str(int(total/freq))
        final = ','.join(words1)
        readData[readData.index(i1)]=final

    
    if words1[3][:len(words1[3])-2]=='NA':
        fgh=words1[0]
        d={}

        for i2 in readData:
            words2=i2.split(',')
            m=words2[3][:len(words2[3])-2]
            if words2[0]==fgh and m!='NA':
                if m in d:
                    d[m]+=1
                else: d[m]=1
                
        max_val = max(d.values())
        for i in d:
            if d[i]==max_val:
                words2[3]=str(i+words2[3][len(words2[3])-2:])
                readData[readData.index(','.join(words1))]=','.join(words2)
                break
        

f1.close()

f2=codecs.open('outclean.csv','w',encoding='utf-8')
for i in readData:
    f2.write(i)
f2.close()

print('Cleaning Done...')
