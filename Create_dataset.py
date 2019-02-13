
"""web for dataset information :-
http://vikaspedia.in/agriculture/livestock/cattle-buffalo/breeds-of-cattle-buffalo"""


import random
import codecs
import pandas as pd

cows = ['गिर','लाल सिंधी','देओनी','हरिआना','गिर','नीली रवि ','मेहसाना','नागपुरी']
rem = ['ಕನ್ನಡ್','عرب','বাংলা','தமிழ்','български']

final_data=''

for i in range(0,1000):
    choice = random.choice(cows)
    milk_yeild=0
    calving=0
    color=''
    
    if choice=='गिर':
        milk_yeild = random.randint(1200,1800) 
        calving = random.randint(45,54)
        color = random.choice(['white','brown','black'])
        
    elif choice=='लाल सिंधी':
        milk_yeild = random.randint(1100,2600) 
        calving = random.randint(30,50)
        color = random.choice(['white','brownish-red','black'])
        
    elif choice=='देओनी':
        milk_yeild = random.randint(600,1200) 
        calving = random.randint(3,5)
        color = random.choice(['white','brown','spotted-black'])
        
    elif choice=='हरिआना':
        milk_yeild = random.randint(600,800) 
        calving = random.randint(40,60)
        color = random.choice(['white','black'])
                
    elif choice=='गिर':
        milk_yeild = random.randint(1000,1100) 
        calving = random.randint(38,40)
        color = random.choice(['brown','black'])
        
    elif choice=='नीली रवि ':
        milk_yeild = random.randint(1500,1850) 
        calving = random.randint(16,18)
        color = random.choice(['white','black'])
        
    elif choice=='मेहसाना':
        milk_yeild = random.randint(1200,1500) 
        calving = random.randint(15,17)
        color = random.choice(['whittish-brown','brown','black'])
        
    elif choice=='नागपुरी':
        milk_yeild = random.randint(1800,1900) 
        calving = random.randint(45,52)
        color = random.choice(['white','brown','blackish-brown'])
        
    else: pass
    
    l = [choice,str(milk_yeild),str(calving),color ]
    temp_data = ','.join(l)
    final_data+=temp_data+'\n'

f = codecs.open('data.csv','w',encoding='utf-8')
d=['Cow','Milk','Calving','Skin Color']
f.write(','.join(d)+'\n')
f.write(final_data)
f.close()

df = pd.read_csv('data.csv')

col1 = list(df.iloc[:,0])
for i in range(0,2):
    col1[i] = random.choice(rem)
for i in range(0,8):
    t=random.randint(3,len(col1)-1)
    col1[t]=random.choice(rem)

col2 = list(df.iloc[:,1])
for i in range(0,20):
    t=random.randint(0,len(col2)-1)
    col2[t] = 'NA'


col3 = list(df.iloc[:,2])
for i in range(0,30):
    t=random.randint(0,len(col3)-1)
    col3[t] = 'NA'


col4 = list(df.iloc[:,3])
for i in range(0,30):
    t=random.randint(0,len(col4)-1)
    col4[t] = 'NA'

df['Cow']=col1    
df['Milk']=col2
df['Calving']=col3
df['Skin Color']=col4
df.to_csv('out.csv', sep=',', encoding='utf-8',index=False)
