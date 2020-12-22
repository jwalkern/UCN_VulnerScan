# -*- coding: utf-8 -*-

from flask import render_template
from app import app
import matplotlib.pyplot as plt
from app import driver



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def jquery():
    return render_template('docs.html')

 
@app.route("/scan", methods=["GET"])
def resultView():
    xmlFile = driver.nmap_scan()
    
    # xmlFile = '/home/pi/vulnerScan/website/app/static/files/result.xml'
    hosts = driver.xml_reader(xmlFile)
    counter = 0
    for host in hosts:
    
        counter += 1
        filePath = f"/home/pi/vulnerScan/website/app/static/images/plot{counter}.png"
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
        port = chartPorts
        vExploits = verifiedExploits
        pExploits = possibleExploits
        # the width of the bars: can also be len(x) sequence
        
        fig, ax = plt.subplots()
        width = 0.35   
        ax.bar(port, vExploits, width, label='Not confirmed exploits')
        ax.bar(port, pExploits, width, bottom=vExploits,
               label='Exploits')
        
        ax.set_ylabel('Exploits')
        ax.set_title(title)
        
        plt.savefig(filePath)
        plt.clf()
 
 
    
    return render_template("docs.html")