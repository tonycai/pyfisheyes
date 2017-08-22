from pychartdir import *
import logging
log = logging.getLogger(__name__)

class BorderlessBarChart:
    
    def __init__(self,l,names,titles,opt="0",dset=""):
        # The data for the bar chart
#        data = [3.9, 8.1, 10.9, 14.2, 18.1, 19.0, 21.2, 23.2, 25.7, 36]
        
        # The labels for the bar chart
#        labels = ["Bastic Group", "Simpa", "YG Super", "CID", "Giga Tech", "Indo Digital","Supreme", "Electech", "THP Thunder", "Flash Light"]
        labels = []
        data = []
        i=0
        item_name_len = 0
        item_name_len_tmp = 0
        for i,r in enumerate(l):
            mediadata = str(r.mediadata)
            ds =  mediadata.split(',')
            labels.append(str(ds[1]))
            item_name_len_tmp = len(str(ds[1]))
            if item_name_len_tmp > item_name_len:
                item_name_len = item_name_len_tmp
            data.append(ds[2])            
                        
        self.width = 700
        self.height = 0
        if i > 30:
            self.steplength = 18
        else:
            self.steplength = 24
        self.height = self.steplength * ( i + 1 )
        # Create a XYChart object of size 600 x 250 pixels
        self.c = XYChart(self.width, self.height)
        
        # Add a title to the chart using Arial Bold Italic font
        self.c.addTitle(str(titles[0])+" - "+ str(dset), "arialbi.ttf")
        
        # Set the plotarea at (100, 30) and of size 400 x 200 pixels. Set the plotarea
        # border, background and grid lines to Transparent
        item_name_len = (item_name_len*9)
        log.debug("item_name_len: "+str(item_name_len))
        self.c.setPlotArea(item_name_len, 30, self.width-(item_name_len+100), self.height-50, Transparent, Transparent, Transparent, Transparent,Transparent)
        
        # Add a bar chart layer using the given data. Use a gradient color for the bars,
        # where the gradient is from dark green (0x008000) to white (0xffffff)
        layer = self.c.addBarLayer(data, self.c.gradientColor(item_name_len, 0, self.width-100, 0, 0x6666ff, 0xffffff))
        
        # Swap the axis so that the bars are drawn horizontally
        self.c.swapXY(1)
        
        # Set the bar gap to 10%
        layer.setBarGap(0.1)
        
        # Use the format "US$ xxx millions" as the bar label
        layer.setAggregateLabelFormat("q: {value}")
        
        # Set the bar label font to 10 pts Times Bold Italic/dark red (0x663300)
        layer.setAggregateLabelStyle("timesbi.ttf", 10, 0x663300)
        
        # Set the labels on the x axis
        textbox = self.c.xAxis().setLabels(labels)
        
        # Set the x axis label font to 10pt Arial Bold Italic
        textbox.setFontStyle("arialbi.ttf")
        textbox.setFontSize(10)
        
        # Set the x axis to Transparent, with labels in dark red (0x663300)
        self.c.xAxis().setColors(Transparent, 0x663300)
        
        # Set the y axis and labels to Transparent
        self.c.yAxis().setColors(Transparent, Transparent)
        
        

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)