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
import xml_driver
 
app = Flask(__name__)
 
 
 
@app.route("/mysuperplot", methods=["GET"])
def plotView():
 
        
    # Generate plot
    port = ['P21', 'P22', 'P80', 'P139', '145']
    men_means = [20, 35, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]
    men_std = [2, 3, 4, 1, 2]
    women_std = [3, 5, 2, 3, 3]
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    fig, ax = plt.subplots()
    
    ax.bar(port, men_means, width, yerr=men_std, label='Active Exploits')
    ax.bar(port, women_means, width, yerr=women_std, bottom=men_means,
           label='Non active Exploits')
    
    ax.set_ylabel('Exploits')
    ax.set_title('Ip-Adresse')
    ax.legend()
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template("image.html", image=pngImageB64String, title="welcome")
 
 
 
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)