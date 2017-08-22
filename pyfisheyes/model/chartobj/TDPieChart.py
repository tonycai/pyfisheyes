from pychartdir import *

class TDPieChart:
    
    def __init__(self):
        # The data for the pie chart
        data = [25, 18, 15, 12, 8, 30, 35]
        
        # The labels for the pie chart
        labels = ["Labor", "Licenses", "Taxes", "Legal", "Insurance", "Facilities",
            "Production"]
        
        # Create a PieChart object of size 360 x 300 pixels
        self.c = PieChart(360, 300)
        
        # Set the center of the pie at (180, 140) and the radius to 100 pixels
        self.c.setPieSize(180, 140, 100)
        
        # Add a title to the pie chart
        self.c.addTitle("Project Cost Breakdown")
        
        # Draw the pie in 3D
        self.c.set3D()
        
        # Set the pie data and the pie labels
        self.c.setData(data, labels)
        
        # Explode the 1st sector (index = 0)
        self.c.setExplode(0)

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)