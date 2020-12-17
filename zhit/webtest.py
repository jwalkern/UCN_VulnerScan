#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:57:14 2020
 
@author: jamibrch
"""
 
from flask import Flask, render_template
import io
import base64
import matplotlib.pyplot as plt


from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

 
app = Flask(__name__)
 
 
 
@app.route("/", methods=["GET"])
def plotView():
    
    from xml_driver import xml_driver

    xmlFile = 'test.xml'
    
    hosts = xml_driver(xmlFile)
    counter = 0
    # totalCriticalExploits = 0
    # totalPossibleExploits = 0
    
    for host in hosts:
        
        counter += 1
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
    
    
        width = 0.35       # the width of the bars: can also be len(x) sequence
        
        fig, ax = plt.subplots()
        
        ax.bar(chartPorts, possibleExploits, width, label='Exploits')
        ax.bar(chartPorts, verifiedExploits, width, bottom=possibleExploits,
               label='Active Exploits')
        
        ax.set_ylabel('Exploits')
        ax.set_title(title)
        ax.legend()
        
        plt.figure(counter)
        
    plt.show()
        
    return render_template('image.html', image=plt.show)
 
 
 
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)