#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:57:14 2020
 
@author: jamibrch
"""
 
import matplotlib.pyplot as plt
from xml_driver import xml_reader
import numpy.random as rd
import pandas as pd


 
hosts = xml_reader('test.xml')
counter = 0


for host in hosts:
    
    counter += 1
    
    title = host['address']
    
    chartPorts = []
    verifiedExploits = []
    possibleExploits = []
    
    
    
    if 'ports' in host:
        for port in host['ports']:
            
            chartPorts.append(port['port'])
            if 'active exploits:' in port:
                verifiedExploits.append(port['active exploits:'])
            else:
                verifiedExploits.append(0)
                
            if 'exploits:' in port:
                possibleExploits.append(port['exploits:'])
            else:
                possibleExploits.append(0)
 
    
        # Generate plot

        # the width of the bars: can also be len(x) sequence
        
        fig, ax = plt.subplots()
        width = 0.35   
        ax.bar(chartPorts, verifiedExploits, width, label='Not confirmed exploits')
        ax.bar(chartPorts, possibleExploits, width, bottom=verifiedExploits,
               label='Exploits')
        
        ax.set_ylabel('Exploits')
        ax.set_title(title)
        
        ax.legend()
    
plt.show() 

for host in hosts:
    print('---------------------------------------------------------')
    print('Name:', str(host.get('name','')))
    print('IP:', str(host.get('address', '')))
    print('Services: ')
    for port in host['ports']:
        print('\t Service: ')
        print('\t-----------------------------------')
        for k,v in port.items():
            print('\t\t',str(k),':',str(v))
    print('---------------------------------------------------------')     
    
    

    

