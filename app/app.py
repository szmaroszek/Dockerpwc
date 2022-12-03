from flask import Flask, request, escape
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
app = Flask(__name__)
@app.route('/print-plot')
def plot_png():
    x = np.linspace(-100,100,1000)
    y = int(request.args.get('a'))*x**2 + int(request.args.get('b'))*x + int(request.args.get('c'))
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(x, y)
    axis.set_xlim((int(request.args.get('xmin')), int(request.args.get('xmax'))))
    axis.set_ylim((int(request.args.get('ymin')), int(request.args.get('ymax'))))
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


