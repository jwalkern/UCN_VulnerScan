# -*- coding: utf-8 -*-

from flask import render_template
from app import app
import io
import base64
import matplotlib.pyplot as plt


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

    
    