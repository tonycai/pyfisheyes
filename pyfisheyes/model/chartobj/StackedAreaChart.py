from pychartdir import *

class StackedAreaChart:
    
    def __init__(self):
        # The data for the area chart
        data0 = [42, 49, 33, 38, 51, 46, 29, 41, 44, 57, 59, 52, 37, 34, 51, 56, 56, 60, 70,
            76, 63, 67, 75, 64, 51]
        data1 = [50, 45, 47, 34, 42, 49, 63, 62, 73, 59, 56, 50, 64, 60, 67, 67, 58, 59, 73,
            77, 84, 82, 80, 84, 89]
        
        labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
            "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
        
        # Create a XYChart object of size 300 x 210 pixels. Set the background to pale yellow
        # (0xffffc0) with a black border (0x0)
        self.width = 700
        self.height = 250
        self.c = XYChart(self.width, self.height, 0xffffc0, 0x000000)
        
        # Set the plotarea at (50, 30) and of size 240 x 140 pixels. Use white (0xffffff)
        # background.
        self.c.setPlotArea(50, 30, self.width-60, self.height-70).setBackground(0xffffff)
        
        # Add a legend box at (50, 185) (below of plot area) using horizontal layout. Use 8
        # pts Arial font with Transparent background.
        self.c.addLegend(50, self.height-30, 0, "", 8).setBackground(Transparent)
        
        # Add a title box to the chart using 8 pts Arial Bold font, with yellow (0xffff40)
        # background and a black border (0x0)
        self.c.addTitle("Sales Volume", "arialbd.ttf", 8).setBackground(0xffff40, 0)
        
        # Set the y axis label format to US$nnnn
        self.c.yAxis().setLabelFormat("US${value}")
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(labels)
        
        # Display 1 out of 2 labels on the x-axis. Show minor ticks for remaining labels.
        self.c.xAxis().setLabelStep(2, 1)
        
        # Add an stack area layer with three data sets
        layer = self.c.addAreaLayer2(Stack)
        layer.addDataSet(data0, 0x4040ff, "Store #1")
        layer.addDataSet(data1, 0xff4040, "Store #2")
        

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)