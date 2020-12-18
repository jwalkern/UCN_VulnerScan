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

test = {}

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5)
width = .5


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
                
     
    
   
    test[title] = [chartPorts,  possibleExploits, verifiedExploits]


    
for i in range(len(test)):
    x = 's{}'.format(i)
    ax = 'ax{}'.format(i)
    
    x = pd.Series(rd.randint(10, size=rd.randint(1, 10)))
    x.plot(kind='bar', width=width, ax=ax)
    ax.set_xlim([-width, (2 + len(x)) * width])
    # ax.set_xlim([-.5, max(len(s1), len(s2)) - 1 + width])
    
plt.show()    
    
    
    
    # width = 0.35       # the width of the bars: can also be len(x) sequence            
    # plt.figure()
        
    
    # fig, ax = plt.subplots()
    
    
    # ax.bar(chartPorts, possibleExploits, width, label='Exploits', align='center')
    # ax.bar(chartPorts, verifiedExploits, width, bottom=possibleExploits,
    #         label='Active Exploits')
    
    # ax.set_ylabel('Exploits')
    # ax.set_title(title)
    





# s1 = pd.Series(rd.randint(10, size=rd.randint(1, 10)))
# s2 = pd.Series(rd.randint(10, size=rd.randint(1, 10)))
# s3 = pd.Series(rd.randint(10, size=rd.randint(1, 10)))
# s4 = pd.Series(rd.randint(10, size=rd.randint(1, 10)))
# s5 = pd.Series(rd.randint(10, size=rd.randint(1, 10)))


# s1.plot(kind='bar', width=width, ax=ax1)
# s2.plot(kind='bar', width=width, ax=ax2)
# s3.plot(kind='bar', width=width, ax=ax3)
# s4.plot(kind='bar', width=width, ax=ax4)
# s5.plot(kind='bar', width=width, ax=ax5)


# ax1.set_xlim([-width, (2 + len(s2)) * width])
# ax2.set_xlim([-width, (2 + len(s2)) * width])
# ax3.set_xlim([-width, (2 + len(s2)) * width])
# ax4.set_xlim([-width, (2 + len(s2)) * width])
# ax5.set_xlim([-width, (2 + len(s2)) * width])


# ax1.set_xlim([-.5, max(len(s1), len(s2)) - 1 + width])
# ax2.set_xlim([-.5, max(len(s1), len(s2)) - 1 + width])        
# ax3.set_xlim([-.5, max(len(s1), len(s2)) - 1 + width])
# ax4.set_xlim([-.5, max(len(s1), len(s2)) - 1 + width])      
# ax5.set_xlim([-.5, max(len(s1), len(s2)) - 1 + width])
     

# plt.show()    

    


# print(test)