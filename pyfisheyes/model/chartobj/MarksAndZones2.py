from pychartdir import *
import logging
log = logging.getLogger(__name__)

class MarksAndZones2:
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
        
        # Create a XYChart object of size 400 x 270 pixels
        self.width = self.f_width #660
        self.height = self.f_height #250
        self.c = XYChart(self.width, self.height)
        
        
        self.critical_color = 0xff0000
        self.warning_color = 0xff9900
        
        # Set the plotarea at (80, 25) and of size 300 x 200 pixels. Use alternate color
        # background (0xeeeeee) and (0xffffff). Set border and grid colors to grey
        # (0xc0c0c0).
        self.c.setPlotArea(60, 25, self.width - 70, self.height - 60, 0xeeeeee, 0xffffff, 0xc0c0c0, 0xc0c0c0, 0xc0c0c0)
        
        # Add a title to the chart using 14 pts Times Bold Italic font
        self.c.addTitle(str(self.titles[0]) , "timesbi.ttf", 14)
        
        # Add a title to the y axis
        self.c.yAxis().setTitle(str(self.titles[1]))
        self.c.xAxis().setTitle(str(self.titles[2]) + " (" + str(self.width) + "x" + str(self.height) + ")")
        
        # Set the y axis width to 2 pixels
        self.c.yAxis().setWidth(2)
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(data2['labels'])
        
        # Add a legend box (50, 10) (top of plot area) using horizontal layout. Use 8 pts
        # Arial font. Disable bounding box (set border to transparent).
        
        #legendBox = self.c.addLegend(60, 20, 0, "", 8)
        #legendBox.setBackground(Transparent)
        
        
        
        # Display 1 out of 3 labels on the x-axis. Show minor ticks for remaining labels.
        #(660 - 70) / 10
        #(6600 - 70) / 10
        
        step = data2['n'] / ((self.width - 70) / 49)
        if step < 2:
            step = 2
        self.c.xAxis().setLabelStep(step, step / 2)
        
        # Set the x axis width to 2 pixels
        self.c.xAxis().setWidth(2)
        
        if self.critical > 0:
            #Critical
            # Add a horizontal red (0x800080) mark line at y = 50000
            yMark2 = self.c.yAxis().addMark(self.critical, self.critical_color, "Critical Threshold Set Point")
            
            # Set the mark line width to 2 pixels
            yMark2.setLineWidth(2)
            
            # Put the mark label at the top center of the mark line
            yMark2.setAlignment(TopLeft)
        
        if self.warning > 0:
            #Warning
            # Add a horizontal red (0x800080) mark line at y = 30000
            yMark1 = self.c.yAxis().addMark(self.warning, self.warning_color, "Warning Threshold Set Point")
            
            # Set the mark line width to 2 pixels
            yMark1.setLineWidth(2)
            
            # Put the mark label at the top center of the mark line
            yMark1.setAlignment(TopLeft)
        
        if self.marks:
            
            # Add an orange (0xffcc66) zone from x = 18 to x = 20
            self.c.xAxis().addZone(18, 20, 0xffcc66)
            
            # Add a vertical brown (0x995500) mark line at x = 18
            xMark1 = self.c.xAxis().addMark(18, 0x995500, "Backup Start")
            
            # Set the mark line width to 2 pixels
            xMark1.setLineWidth(2)
            
            # Put the mark label at the left of the mark line
            xMark1.setAlignment(Left)
            
            # Rotate the mark label by 90 degrees so it draws vertically
            xMark1.setFontAngle(90)
            
            # Add a vertical brown (0x995500) mark line at x = 20
            xMark2 = self.c.xAxis().addMark(20, 0x995500, "Backup End")
            
            # Set the mark line width to 2 pixels
            xMark2.setLineWidth(2)
            
            # Put the mark label at the right of the mark line
            xMark2.setAlignment(Right)
            
            # Rotate the mark label by 90 degrees so it draws vertically
            xMark2.setFontAngle(90)
        
        # Add a green (0x00cc00) line layer with line width of 2 pixels
        self.c.addLineLayer(data1['data'], self.line1_color, 'today').setLineWidth(1)
        self.c.addLineLayer(data2['data'], self.line2_color, 'x').setLineWidth(1)
        #0x779C4F
        #0x999999
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
                for k, v in sorted(labs.iteritems()):
                    labels.append(k[11:16])
                    data.append(v)
                    n += 1
                log.debug("n:" + str(n))
        except:
            pass
        return {'data':data, 'labels':labels, 'n':n}
