from pychartdir import *
import logging
log = logging.getLogger(__name__)

class XZoneColoring:
    
    def __init__(self, et, ys=""):
        self.l1 = et[0] 
        self.l2 = et[1] 
        self.labs1 = et[2] 
        self.labs2 = et[3] 
        self.titles = et[4] 
        self.critical = et[5] 
        self.warning = et[6] 
        self.marks = et[7]
        self.line1_color = et[8]
        self.line2_color = et[9]
        self.r_mode = et[10]
        self.helth_range = et[11]
        self.f_width = et[12]
        self.f_height = et[13]
        self.ys = ys
        data1 = self.__datafact__(self.l1, self.labs1, True)
        data2 = self.__datafact__(self.l2, self.labs2, True)

        # Create a XYChart object of size 550 x 220 pixels
        self.width = self.f_width #660
        self.height = self.f_height #250
        
        self.c = XYChart(self.width, self.height)
        
        # Set the plot area at (50, 10) and of size 480 x 180 pixels. Enabled both vertical
        # and horizontal grids by setting their colors to light grey (cccccc)
        self.c.setPlotArea(60, 25, self.width - 70, self.height - 60).setGridColor(0xcccccc, 0xcccccc, 0xc0c0c0, 0xc0c0c0)
        
        # Add a legend box (50, 10) (top of plot area) using horizontal layout. Use 8 pts
        # Arial font. Disable bounding box (set border to transparent).
        legendBox = self.c.addLegend(60, 20, 0, "", 8)
        legendBox.setBackground(Transparent)
        
        # Add keys to the legend box to explain the color zones
        #legendBox.addKey("today", 0x333399)
        legendBox.addKey("Tolerant", self.line2_color) #tolerant Historical
        #legendBox.addKey("Forecast", 0xff9966)
        
        # Add a title to the y axis.
        self.c.addTitle(str(self.titles[0]), "timesbi.ttf", 14)
        self.c.yAxis().setTitle(str(self.titles[1]))        
        self.c.xAxis().setTitle(str(self.titles[2]) + " (" + str(self.width) + "x" + str(self.height) + ")")
        
        # Set the labels on the x axis
        #self.c.xAxis().setLabels2(data2['labels'])
        self.c.xAxis().setLabels(data2['labels'])
        
        # Set multi-style axis label formatting. Use Arial Bold font for yearly labels and
        # display them as "yyyy". Use default font for monthly labels and display them as
        # "mmm". Replace some labels with minor ticks to ensure the labels are at least 3
        # units apart.
        step = data2['n'] / ((self.width - 70) / 49)
        if step < 2:
            step = 2
        #self.c.xAxis().setMultiFormat(StartOfHourFilter(), "{value|hh:mm}", StartOfHourFilter(), "{value|hh:00}")
        self.c.xAxis().setLabelStep(step, step / 2)
        
        #self.c.xAxis().setLabelStep(step, step / 2)
        
        # Add a line layer to the chart
        layer = self.c.addLineLayer2()
        
        # Create the color to draw the data line. The line is blue (0x333399) to the left of
        # x = 18, and become a red (0xd04040) dash line to the right of x = 18.
        lineColor = layer.xZoneColor(1441, self.line1_color, self.c.dashLineColor(0xd04040, DashLine)) #0x333399
        
        # Add the data line
        layer.addDataSet(data1['data'], lineColor)
        
        # Create the color to draw the err zone. The color is semi-transparent blue
        # (0x809999ff) to the left of x = 18, and become semi-transparent red (0x80ff9966) to
        # the right of x = 18.
        errColor = layer.xZoneColor(1441, self.line2_color, 0x80ff9966L) #0x809999ffL
        
        # Add the upper border of the err zone
        layer.addDataSet(ArrayMath(data2['data']).add(data2['heldata']).result(), errColor)
        
        # Add the lower border of the err zone
        layer.addDataSet(ArrayMath(data2['data']).sub(data2['heldata']).result(), errColor)
        
        # Set the default line width to 2 pixels
        layer.setLineWidth(1)
        
        # Color the region between the err zone lines
        self.c.addInterLineLayer(layer.getLine(1), layer.getLine(2), errColor)       
        if self.ys:
            ys = int(self.ys)
            self.c.yAxis().setLinearScale(0, ys)
            self.c.setClipping()
    
    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
    
    def __datafact__(self, l1, labs, ulab):
        data = []
        labels = []
        heldata = []
        i = 0
        n = 0
        try:
            for i, r in enumerate(l1): 
                        
                hour = "%02d" % r.houri
                minute = "%02d" % r.minutei
                key = str(r.datei) + ":" + hour + ":" + minute
                #log.debug(key)       
                if key in labs.keys():
                    labs[key] = r.valuei
            if ulab:
                data = []
                labels = []
                heldata = []
                for k, v in sorted(labs.iteritems()):
                    #labels.append(chartTime(int(k[0:4]), int(k[5:7]), int(k[8:10]), k[11:13], k[14:16], 0))
                    labels.append(k[11:16])
                    data.append(v)
                    heldata.append(v * self.helth_range/100)
                    n += 1
                log.debug("n:" + str(n))
        except:
            log.error("valuei excetion")
        return {'data':data, 'heldata':heldata, 'labels':labels, 'n':n}
    
