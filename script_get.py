# -*- coding:utf-8 -*-
f = open(r'C:\Users\Kismet\Documents\Scripts\Dangal.src')
f1 = open(r'C:\Users\Kismet\Documents\Scripts\Dangal.txt','w')
for i,j in enumerate(f):
    if i%4 == 2:
        f1.write(j.strip()+ '\n')

f.close()
f1.close()