# -*- coding: utf-8 -*-
from pychartdir import *
import logging
log = logging.getLogger(__name__)

class MultiLineChart:
    
    def __init__(self,l,names,titles,opt="0",d="",d2=""):
        # The data for the line chart
        #names = ['datei','com_update','com_insert','com_delete','com_replace']
        #names = ['datei','com_update','com_insert']

        #titles = ['','queries per day','Jun 12, 2010']

        #for na in range(len(names)):
        #    print na,names[na],"test"
        opts = opt.split(',')
        data = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        i = 0
        
        try:
            for i,r in enumerate(l):
                mediadata = str(r.mediadata)
                ds =  mediadata.split(',')
                for na in range(len(names)):
                    it = str(ds[na])
                    if it == "":
                        it = "0"
                    data[str(na)].append(it)                
        except:
            data['0'] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
            data['1'] = [42, 49, 33, 38, 51, 46, 29, 41, 44, 57, 59, 52, 37, 34, 51, 56, 56, 60, 70, 76, 63, 67, 75, 64, 51]
            i = 24
        
        # The data for the line chart
        #self.data0 = [42, 49, 33, 38, 51, 46, 29, 41, 44, 57, 59, 52, 37, 34, 51, 56, 56, 60, 70, 76, 63, 67, 75, 64, 51]
        #self.data1 = [50, 55, 47, 34, 42, 49, 63, 62, 73, 59, 56, 50, 64, 60, 67, 67, 58, 59, 73, 77, 84, 82, 80, 84, 98]
        #self.data2 = [36, 28, 25, 33, 38, 20, 22, 30, 25, 33, 30, 24, 28, 15, 21, 26, 46, 42, 48, 45, 43, 52, 64, 60, 70]
        
        # The labels for the line chart
        self.labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
        
        # Create an XYChart object of size 600 x 300 pixels, with a light blue (EEEEFF)
        # background, black border, 1 pxiel 3D border effect and rounded corners
        
        self.width = 700
        self.height = 250
        
        self.c = XYChart(self.width, self.height, 0xeeeeff, 0x000000, 1)
        self.c.setRoundedFrame()
        
        # Set the plotarea at (55, 58) and of size 520 x 195 pixels, with white background.
        # Turn on both horizontal and vertical grid lines with light grey color (0xcccccc)
        self.c.setPlotArea(80, 58, self.width-120, self.height-100, 0xffffff, -1, -1, 0xcccccc, 0xcccccc)
        
        # Add a legend box at (50, 30) (top of the chart) with horizontal layout. Use 9 pts
        # Arial Bold font. Set the background and border color to Transparent.
        self.c.addLegend(70, 30, 0, "arialbd.ttf", 9).setBackground(Transparent)
        
        # Add a title box to the chart using 15 pts Times Bold Italic font, on a light blue
        # (CCCCFF) background with glass effect. white (0xffffff) on a dark red (0x800000)
        # background, with a 1 pixel 3D border.
        #self.c.addTitle("Application Server Throughput", "timesbi.ttf", 15).setBackground( 0xccccff, 0x000000, glassEffect())
        self.c.addTitle(str(titles[0]), "timesbi.ttf", 15).setBackground( 0xccccff, 0x000000, glassEffect())
        
        # Add a title to the y axis
        self.c.yAxis().setTitle(str(titles[1]))
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(data['0'])
        
        # Display 1 out of 3 labels on the x-axis.
        step = int( i / 6 )
        if step < 2:
            step = 2
        self.c.xAxis().setLabelStep(step, 0)
        
        # Add a title to the x axis
        

        self.c.xAxis().setTitle("From "+str(d)+" To "+str(d2))
        
        # Add a line layer to the chart
        self.layer = self.c.addLineLayer2()
        
        # Set the default line width to 2 pixels
        self.layer.setLineWidth(2)
        
        # Add the three data sets to the line layer. For demo purpose, we use a dash line
        # color for the last line
        for na in range(len(names)):            
            if na > 0:
                if str(na) not in opts:
                    try:
                        self.layer.addDataSet(data[str(na)], self.__colorsschema__(na), str(names[na]))
                    except:
                        log.info("data format error")
                        
        
    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
    
    def __colorsschema__(self,idx):
        v = "#3366FF"
        colors1 = [0x3366FF,0x6633FF,0xCC33FF,0xFF33CC,0x33CCFF,0x003DF5,0x002EB8,0xFF3366,0x33FFCC,0xB88A00,0xF5B800,0xFF6633]
        colors2 = [0x66CCFF,0xFF0000,0x00FF00,0x0000FF,0xCC00FF,0x6699FF,0x009999,0xCCCC00,0xFFCC33,0xFF9999,0x339900,0xCC0066]
        v = colors2[idx]
        return v