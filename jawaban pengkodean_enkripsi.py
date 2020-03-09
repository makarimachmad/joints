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
    
    for i in range(0, len(bantu)):
    
        if i%2 == 0:
            #b = bantu[0]
            print( i, bantu[i])
            genap.append(bantu[i])
            genapdic[i] = bantu[i]
        if i%2 == 1:
            print( i, bantu[i])
            ganjil.append(bantu[i])
            ganjildic[i] = bantu[i]
            
    print(genap,"---", ganjil)
    print("ini apa",b)
    print(genapdic,"......",ganjildic)
    
    
    for key, value in genapdic.items():
        
        b =  (value * int(key+1)) + b
        print(key, b)
    
    for key, value in ganjildic.items():
        b = b + (value * int(key+1))
        print(b)
    
    print(b)

variabel= 'indonesia'
enkripsi(variabel)