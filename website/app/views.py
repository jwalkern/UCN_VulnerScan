# -*- coding: utf-8 -*-

from flask import render_template
from app import app
import io
import base64
import matplotlib.pyplot as plt
from app import xml_driver as x

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/myplot", methods=['GET'])
def plotView():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("title")
    axis.set_xlabel("x-axis")
    axis.set_ylabel("y-axis")
    axis.grid()
    axis.plot(range(5), range(5), "ro-")
    
    # Convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    
    # Encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    return render_template('image.html', image=pngImageB64String)

@app.route('/nmap')
def nmap_result():
    host = x.xml_read('text.xml')
    pass

@app.route('/test')
def sojle():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men_means = [20, 35, 30, 35, 27]
    women_means = [25, 32, 34, 20, 25]
    width = 0.35       # the width of the bars: can also be len(x) sequence
    
    fig, ax = plt.subplots()
    
    ax.bar(labels, men_means, width, label='Men')
    ax.bar(labels, women_means, width, bottom=men_means,
           label='Women')
    
    ax.set_ylabel('Scores')
    ax.set_title('Scores by group and gender')
    ax.legend()
    
    plt.show()
    
    return render_template("test.html", graf=plt.show())
    
    