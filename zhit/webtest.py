#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:57:14 2020
 
@author: jamibrch
"""
 
from flask import Flask, render_template

import matplotlib.pyplot as plt
from xml_driver import xml_reader


 
app = Flask(__name__)
 
 
 
@app.route("/", methods=["GET"])
def plotView():
    # from matplotlib import pyplot as PLT

    # fig = PLT.figure()
    
    # ax1 = fig.add_subplot(211)
    # ax1.plot([(1, 2), (3, 4)], [(4, 3), (2, 3)])
    
    # ax2 = fig.add_subplot(212)
    # ax2.plot([(7, 2), (5, 3)], [(1, 6), (9, 5)])
    
    # PLT.show()
    
   
    hosts = xml_reader('test.xml')
    counter = 0
    
    
    for host in hosts:
        
        counter += 1
        filePath = f'/static/images/plot{counter}.png'
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
    
    
        width = 0.35       # the width of the bars: can also be len(x) sequence
        
        fig, ax = plt.subplots()
        
        
        ax.bar(chartPorts, possibleExploits, width, label='Exploits')
        ax.bar(chartPorts, verifiedExploits, width, bottom=possibleExploits,
                label='Active Exploits')
        
        ax.set_ylabel('Exploits')
        ax.set_title(title)
        
        plt.savefig(filePath)
        
        
        
        
    plt.show()
    
        
    return render_template('image.html', image=plt.show())
 
 
 
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)