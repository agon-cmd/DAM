# -*- coding: utf-8 -*- 
'''
Created on 25 de ene. de 2016

'''
#while
entrada=""
while True:                 
    entrada = raw_input("> ")         
    if entrada == "salir": 
        break 
    else: 
        print entrada

#for
tVall =(1,2,3,4,5)
for ele in tVall:
    if ele % 2 == 0: print str(ele) + " es par"

#Simular bucle for vueltas fijas 
for ele in range(5, 25):
    print "Valor:", ele
