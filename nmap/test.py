#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:57:14 2020
 
@author: jamibrch
"""
 
import matplotlib.pyplot as plt
from xml_driver import xml_reader



 
hosts = xml_reader('test.xml')
counter = 0

test = {}

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
    
                
    plt.figure()
    
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    fig, ax = plt.subplots(1+counter+1)
    
    
    ax.bar(chartPorts, possibleExploits, width, label='Exploits')
    ax.bar(chartPorts, verifiedExploits, width, bottom=possibleExploits,
            label='Active Exploits')
    
    ax.set_ylabel('Exploits')
    ax.set_title(title)
        
    
    test[title] = [chartPorts,  possibleExploits, verifiedExploits]

plt.show()    

    


print(test)