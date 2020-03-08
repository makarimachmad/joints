# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:00:16 2020

@author: FUJITSU
"""

def nomordua(n, m, x):
    
    bantu = []
    gabung = ''
    
    print(n,m,x)
    for i in range(1, n+1):
        bantu.append(i)
    bantu = [str(x) for x in bantu]
    
    gabung = ''.join(str(x) for x in bantu)
    
    print('awal',gabung)
    for i in x:
        if str(i) in gabung:
            gabung = gabung.replace(str(i),'')
    print('penghapusan', gabung)          
    hasil = sum(int(x) for x in gabung)
    print(hasil)      



#mulai dari sini
    
n = int(input("banyak angka: "))
m = int(input("banyak bolong: "))
x = []

for i in range(m):
    nilai = int(input())
    x.append(nilai)

print(x)
nomordua(n,m,x)
    
