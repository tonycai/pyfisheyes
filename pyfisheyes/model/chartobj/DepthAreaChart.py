# -*- coding: utf-8 -*-
from pychartdir import *

class DepthAreaChart:
    
    def __init__(self, l1, l2, names, titles, dset1, dset2, labs):
        # The data1 for the area chart
        
        
        data1 = self.datafact(l1, names, labs)
        data2 = self.datafact(l2, names, labs)
            
        self.width = 700
        self.height = 250
        # Create a XYChart object of size 350 x 230 pixels
        self.c = XYChart(self.width, self.height)
        self.c.setDefaultFonts("simsun.ttc");
        # Set the plotarea at (50, 30) and of size 250 x 150 pixels.
        self.c.setPlotArea(80, 30, self.width - 100, self.height - 80)
        
        # Add a legend box at (55, 0) (top of the chart) using 8 pts Arial Font. Set
        # background and border to Transparent.
        self.c.addLegend(55, 0, 0, "", 8).setBackground(Transparent)
        
        # Add a title to the x axis
        self.c.xAxis().setTitle(str(titles[0]) , "timesbi.ttf", 12)
        
        # Add a title to the y axis
        self.c.yAxis().setTitle(str(titles[1]))
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(data2['labels'])
        
        # Display 1 out of 2 labels on the x-axis. Show minor ticks for remaining labels.
        self.c.xAxis().setLabelStep(2, 1)
        
        # Add three area layers, each representing one data1 set. The areas are drawn in
        # semi-transparent colors.
        
                
        self.c.addAreaLayer(data1['data'], 0x808080ffL, str(dset1), 3) #0x808080ffL
        self.c.addAreaLayer(data2['data'], 0x80ff0000L, '上周同一天', 2) #0x80ff0000L
                    #0x8000ff00L
    
    def datafact(self, l, names, labs):
        data = []
        labels = []
        i = 0
        n = 24
        try:
            for i, r in enumerate(l):
                key = "%02d" % r.houri
                mediadata = str(r.mediadata)
                ds = mediadata.split(',')                
                if key in labs.keys():
                    labs[key] = ds[len(ds)-1]
                    
            for k, v in sorted(labs.iteritems()):
                    labels.append(k)
                    data.append(v)
                    n +=1
            log.debug("n:"+str(n))
        except:
            pass
            
        return {'data':data, 'labels':labels, 'n':n}
    
    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
