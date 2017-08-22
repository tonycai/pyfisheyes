from pychartdir import *

class SimpleBarChart:
    
    def __init__(self):
        # The data for the bar chart
        data = [85, 156, 179.5, 211, 123]
        
        # The labels for the bar chart
        labels = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        
        # Create a XYChart object of size 250 x 250 pixels
        self.c = XYChart(250, 250)
        
        # Set the plotarea at (30, 20) and of size 200 x 200 pixels
        self.c.setPlotArea(30, 20, 200, 200)
        
        # Add a bar chart layer using the given data
        self.c.addBarLayer(data)
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(labels)

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)