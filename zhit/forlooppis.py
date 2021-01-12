# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:59:17 2020

@author: mbvar
"""

from xml_driver import xml_driver

xmlFile = 'test.xml'

hosts = xml_driver(xmlFile)
# counter = 0
# totalCriticalExploits = 0
# totalPossibleExploits = 0

for host in hosts:
    
    # counter += 1
    # filePath = f'/static/images/plot{counter}.png'
    
    title = host['address']
    
    chartPorts = []
    verifiedExploits = []
    possibleExploits = []
    
    if 'ports' in hosts[1]:
        for port in hosts[1]['ports']:
            
            chartPorts.append(port['port'])
            if 'active exploits:' in port:
                verifiedExploits.append(port['active exploits:'])
            else:
                verifiedExploits.append(0)
                
            if 'exploits:' in port:
                possibleExploits.append(port['exploits:'])
            else:
                possibleExploits.append(0)
                



    test[title] = chartPorts,verifiedExploits,possibleExploits