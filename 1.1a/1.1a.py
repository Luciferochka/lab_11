'''
Дани двійкові файли f та g, компоненти яких є цілими числами. Отримати в
файлі h нові компоненти, що утворюються в результаті віднімання двох компонентів
файлів f та g, що знаходяться на відповідних позиціях
'''

first = [7, 32, 15, 23, 13]  

second = [4, 23, 33, 2, 18]  

f = open('f.bin', 'wb')  
g = open('g.bin', 'wb')  

for item in first:  
    s = str(item) + '\n'  
    bt = s.encode()  
    f.write(bt) 

for item in second:  
    s = str(item) + '\n'  
    bt = s.encode()  
    g.write(bt)  

f.close()
g.close

f = open('f.bin', 'rb')
g = open('g.bin', 'rb')

h = open('h.bin', 'wb')  
i = 0  
for ln in f:  
    x = int(ln)  
    first[i] = x  
    i += 1  
j = 0  
for ln in g:  
    x = int(ln) 
    y = first[j] - x  
    bt = str(y).encode() 
    h.write(bt)  
    j += 1  
h.close()  
