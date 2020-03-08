# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:00:16 2020

@author: FUJITSU
"""

# -- enkripsi --

def enkripsi(bantu):
    
    genap = []
    ganjil = []
    b = ''
    
    genapdic = dict()
    ganjildic = dict()
    
    for i in range(1, len(bantu)):
    
        if i%2 == 0:
            b = bantu[0]
            print( i, bantu[i])
            genap.append(bantu[i])
            genapdic[i] = bantu[i]
        if i%2 == 1:
            print( i, bantu[i])
            ganjil.append(bantu[i])
            ganjildic[i] = bantu[i]
            
    #print(genap,"---", ganjil)
    #print(b)
    #print(genapdic,"......",ganjildic)
    
    
    for key, value in genapdic.items():
        b =  (value * int(key+1)) + b
    
    for key, value in ganjildic.items():
        b = b + (value * int(key+1))
    
    print(b)

variabel= 'hans'
enkripsi(variabel)


# ----  dekrip  ----
banyak = int(input("banyak: "))
variabel = []

for i in range(banyak):
    huruf = input()
    variabel.append(huruf)

print(variabel)


def bubblesort(nilai):
    
    nilaiurut = sorted(nilai, key = nilai.get, reverse = False)
    tampung = ''
    for i in nilaiurut:
        tampung = tampung + i
        
    print(tampung)
    print("\n")
    
    
def check_freq(bantu):
    
    from collections import  Counter
    
    b = ''
    
    nilai = Counter(bantu)
    #print(''.join(['{0}{1}'.format(k, v) for k,v in nilai.items()]))
    #print(nilai)
    #print(type(nilai))
    #for key, value in nilai.items():
    #    b = b + key
    #    print(type(value))
    bubblesort(nilai)


def dekrip(x):
    
    for i in range(len(x)):  
        print(x[i])
        #print(type(x[i]))
        check_freq(x[i])
    
    
dekrip(variabel)

