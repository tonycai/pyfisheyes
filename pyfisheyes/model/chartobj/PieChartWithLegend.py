from pychartdir import *

class PieChartWithLegend:
    
    def __init__(self):
        # The data for the pie chart
        data = [25, 18, 15, 12, 8, 30, 35]
        
        # The labels for the pie chart
        labels = ["Labor", "Licenses", "Taxes", "Legal", "Insurance", "Facilities",
            "Production"]
        
        # Create a PieChart object of size 450 x 240 pixels
        self.c = PieChart(450, 240)
        
        # Set the center of the pie at (150, 100) and the radius to 80 pixels
        self.c.setPieSize(150, 100, 80)
        
        # Add a title at the bottom of the chart using Arial Bold Italic font
        self.c.addTitle2(Bottom, "Project Cost Breakdown", "arialbi.ttf")
        
        # Draw the pie in 3D
        self.c.set3D()
        
        # add a legend box where the top left corner is at (330, 40)
        self.c.addLegend(330, 40)
        
        # modify the label format for the sectors to $nnnK (pp.pp%)
        self.c.setLabelFormat("{label} ${value}K\n({percent}%)")
        
        # Set the pie data and the pie labels
        self.c.setData(data, labels)
        
        # Explode the 1st sector (index = 0)
        self.c.setExplode(0)
        

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)