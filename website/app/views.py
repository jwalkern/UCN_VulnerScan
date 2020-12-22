# -*- coding: utf-8 -*-

from flask import render_template
from app import app
import io
import base64
import matplotlib.pyplot as plt
from app import driver


from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas




@app.route('/')
def index():
    return render_template('index.html')


@app.route("/myplot", methods=['GET'])
def plotView():
     # Generate plot
    port = ['P21', 'P22', 'P80', 'P139', '145']
    exploit = [20, 35, 30, 35, 27]
    active_exploit = [25, 32, 34, 20, 25]

    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    fig, ax = plt.subplots()
    
    ax.bar(port, exploit, width, label='Exploits')
    ax.bar(port, active_exploit, width, bottom=exploit,
           label='Active Exploits')
    
    ax.set_ylabel('Exploits')
    ax.set_title('Ip-Adresse')
    ax.legend()
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template('image.html', image=pngImageB64String)

 
@app.route("/result", methods=["GET"])
def resultView():
    xmlFile = '/home/pi/vulnerScan/nmap/test.xml'
    hosts = driver.xml_reader(xmlFile)
    counter = 0
    for host in hosts:
    
        counter += 1
        filePath = f"/home/pi/vulnerScan/website/app/static/plot{counter}.png"
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
                
                ax.legend()
                
                
                
                # # Convert plot to PNG image
                # pngImage = io.BytesIO()
                # FigureCanvas(fig).print_png(pngImage)
                
                # # Encode PNG image to base64 string
                # pngImageB64String = "data:image/png;base64,"
                # pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
               
        plt.savefig(filePath)
        plt.clf()
 
 
    
    return render_template("docs.html")