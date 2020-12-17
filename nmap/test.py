#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:57:14 2020
 
@author: jamibrch
"""
 
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

    
    test[title] = chartPorts, possibleExploits, verifiedExploits
    

print(test)