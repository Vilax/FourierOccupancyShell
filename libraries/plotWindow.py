#!../env/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 01:18:11 2020

@author: vilas
"""

import sys
import matplotlib
import numpy as np
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


def readMetaData(metadataFile):
    file = open(metadataFile, "r")
    lines = file.readlines()
    file.close()

    labels = []
    x = []
    y = []
    md = []
    for line in lines:
        line = line.strip()
        if line[0] == "#":
            continue
        else:
            if str.isalpha(line[0]) is True:
                continue
            else:
                if line[0] == "_":
                    labels.append(line)
                else:
                    md.append(np.fromstring(line, dtype=np.float, sep=' '))
    md = np.stack(md, axis=0)

    md = md.transpose()
    mdDict = dict(zip(labels, md))

    return mdDict

def formatFreq(value, pos):
    """ Format function for Matplotlib formatter. """
    inv = 999.
    if value:
        inv = 1 / value
    return "1/%0.2f" % inv


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100, polar=False):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = None
        if polar:
            self.axes = self.fig.add_subplot(111, projection='polar')
        else:
            self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)


class PlotAgainstResolution(QtWidgets.QMainWindow):

    def __init__(self, mdFile, labelX, labelY, xlabel, ylabel, title, hthresholds):
        super(PlotAgainstResolution, self).__init__()

        self.mdFile = mdFile
        self.labelX = labelX
        self.labelY = labelY
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title
        self.hthresholds = hthresholds

        sc = MplCanvas(self, width=5, height=4, dpi=100, polar=False)
        
        mdDict = readMetaData(self.mdFile)

        x = mdDict[self.labelX]
        y = mdDict[self.labelY]
        from matplotlib.ticker import FuncFormatter
        sc.axes.xaxis.set_major_formatter(FuncFormatter(formatFreq))
        sc.axes.set_ylim([-0.1, 1.1])
        sc.axes.plot(x, y)
        sc.axes.set_xlabel(self.xlabel)
        sc.axes.set_ylabel(self.ylabel)
        sc.axes.set_title(self.title)
        sc.axes.hlines(hthresholds, x[0], x[-1], colors = 'k', linestyles = 'dashed')
        sc.axes.grid(True)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()

        
class PlotAngular(QtWidgets.QMainWindow):

    def __init__(self, mdFile, labelRadial, labelAzimutal, labelCounts, xlabel, ylabel, title):
        super(PlotAngular, self).__init__()

        self.mdFile = mdFile
        self.labelRadial = labelRadial
        self.labelAzimutal = labelAzimutal
        self.labelCounts = labelCounts
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.title = title

        sc = MplCanvas(self, width=5, height=4, dpi=100, polar=True)
        
        mdDict = readMetaData(self.mdFile)

        radius = mdDict[labelRadial]
        azimuth = mdDict[labelAzimutal]
        counts = mdDict[labelCounts]
        
        # define binning
        azimuths = np.radians(np.linspace(0, 360, 360))
        zeniths = np.arange(0, 91, 1)
    
        r, theta = np.meshgrid(zeniths, azimuths)
    
        values = np.zeros((len(azimuths), len(zeniths)))
        
        for i in np.arange(0, len(azimuth)):
            values[int(azimuth[i]), int(radius[i])] = counts[i]

                
        # ------ Plot ------
        stp = 0.1
        lowlim = values.min()
        if ((lowlim - stp)<0):
            lowlim = 0.0
        else:
            lowlim = lowlim - stp

        highlim = values.max() + stp
        pc = sc.axes.contourf(theta, r, values, np.arange(values.min(), highlim, stp))
    
        sc.fig.colorbar(pc)


        sc.axes.set_title(self.title)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()
        
        



    

    



    



    
