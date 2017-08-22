from pychartdir import *

class OverlappingBarChart:
    
    def __init__(self):
        # The data for the bar chart
        data0 = [100, 125, 156, 147, 87, 124, 178, 109, 140, 106, 192, 122, 100, 100, 100, 100, 110, 111, 123, 123]
        
        labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct","Nov", "Dec", "Dec", "Dec", "Dec", "Dec", "Dec", "Dec", "Dec", "Dec"]
        
        self.width = 700
        self.height = 250
        # Create a XYChart object of size 580 x 280 pixels
        self.c = XYChart(self.width, self.height)
        
        # Add a title to the chart using 14 pts Arial Bold Italic font
        self.c.addTitle("DB Server", "arialbi.ttf", 14)
        
        # Set the plot area at (50, 50) and of size 500 x 200. Use two alternative background
        # colors (f8f8f8 and ffffff)
        self.c.setPlotArea(50, 50, 500, 200, 0xf8f8f8, 0xffffff)
        
        # Add a legend box at (50, 25) using horizontal layout. Use 8pts Arial as font, with
        # transparent background.
        self.c.addLegend(50, 25, 0, "arial.ttf", 8).setBackground(Transparent)
        
        # Set the x axis labels
        self.c.xAxis().setLabels(labels)
        
        # Draw the ticks between label positions (instead of at label positions)
        self.c.xAxis().setTickOffset(0.5)
        
        # Add a multi-bar layer with 3 data sets
        layer = self.c.addBarLayer2(Side)
        layer.addDataSet(data0, 0x8080ff, "select")
#        layer.addDataSet(data1, 0x80ff80, "Year 2004")
#        layer.addDataSet(data2, 0x8080ff, "Year 2005")
        
        # Set 50% overlap between bars
        layer.setOverlapRatio(0.5)
        
        # Add a title to the y-axis
        self.c.yAxis().setTitle("Revenue (USD in millions)")

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)