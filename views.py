import codecs

inp=input("Enter file name : ")

f1 = codecs.open(inp,'r',encoding='utf-8')
l=f1.readlines()

for words in l:
    i=words.split(',')
    print('\t'.join(i))
f1.close()    
