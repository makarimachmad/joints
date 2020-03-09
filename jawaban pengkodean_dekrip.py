# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 00:14:10 2020

@author: FUJITSU
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 16:50:25 2020

@author: FUJITSU
"""

banyak = int(input("banyak: "))
variabel = []

for i in range(banyak):
    huruf = input()
    variabel.append(huruf)

print(variabel)

for i in range(banyak):
    
    dekrip(variabel[i])

def dekrip(variabel):
    
    variabeldict = {}

    #for i in range(len(variabel)):
    #    print(variabel[i])
        
    tmp = 0
    
    huruf = ''
    listhuruf = []
    posisi = 0
    banyakhuruf = 0
    hurufdict = {}
    listhuruf = []
    listbanyakhuruf = []
    
    tampungmaks = []
    terakhir = []
    
    for i in range(len(variabel)):
        if huruf != variabel[i]:
            huruf = variabel[i]
            #print("\n","indeks ke",posisi,"\n",huruf)
            posisi = posisi + 1
            listhuruf.append(huruf)
            tampungmaks.append(banyakhuruf)
            terakhir.append(max(tampungmaks))
            tampungmaks = []
            
            #ambil posisi, huruf, maks
            
            banyakhuruf = 0
            
        if huruf == variabel[i]:
            banyakhuruf = banyakhuruf+1
            
            #print(banyakhuruf)
            
    terakhir.append(banyakhuruf)
   
    terakhir.pop(0)       
    #print(terakhir)
    #print(listhuruf)
    
    #print(type(terakhir))
    
    for i in range(0, len(listhuruf)):
        hurufdict[terakhir[i]] = listhuruf[i]
    
    #print(hurufdict)
    #print(type(hurufdict))
    import collections
    
    od = collections.OrderedDict(sorted(hurufdict.items()))
    od = collections.deque(sorted(hurufdict.items()))
    #print(type(od))
    #print(od)
    od = list(od)
    
    hasildekrip = ''
    
    bantu = dict(sorted(hurufdict.items()))
    #print(bantu)
    for key, value in bantu.items():
        hasildekrip = hasildekrip + value
    
    print(hasildekrip)
    
    #return hasildekrip