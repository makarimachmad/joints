# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:00:16 2020

@author: FUJITSU
"""

def nomorsatu(bantu):
    
    for i in range(len(bantu)):
        if i%2 == 0:
            bantu.add('c')
        print( i, bantu[i])
    


variabel= 'makarim'
nomorsatu(variabel)
    
