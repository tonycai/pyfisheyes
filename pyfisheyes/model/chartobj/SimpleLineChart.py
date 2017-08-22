from pychartdir import *
import logging
log = logging.getLogger(__name__)

class SimpleLineChart:
    def __init__(self, et):
        #l1, l2, labs1, labs2, allt
        
        self.l1 = et[0]
        self.l2 = et[1]
        self.labs1 = et[2]
        self.labs2 = et[3]
        self.line1_color = et[4]
        self.line2_color = et[5]
        self.n = 4
        if et[6]:
            self.width = 600
            self.height = 240
            self.n = 9
        else:
            self.width = 300
            self.height = 160
        
        
        
        self.max_value = 0
        
        data1 = self.__datafact__(self.l1, self.labs1, True, True)
        data2 = self.__datafact__(self.l2, self.labs2, True)
        
        
        
        # Create a XYChart object of size 250 x 250 pixels
        self.c = XYChart(self.width, self.height)
        
        # Set the plotarea at (30, 20) and of size 200 x 200 pixels
        self.c.setPlotArea(50, 20, self.width - 80, self.height - 50)
        
        # Add a line chart layer using the given data
        self.c.addLineLayer(data1['data'], self.line1_color, 'today')
        self.c.addLineLayer(data2['data'], self.line2_color, 'yestoday')
        
        #layer.addDataSet(data0, 0xff0000, "Server #1")
        #layer.addDataSet(data1, 0x008800, "Server #2")
        #layer.addDataSet(data2, c.dashLineColor(0x3333ff, DashLine), "Server #3")
        
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(data2['labels'])
        
        step = data2['n'] / self.n
        if step < 2:
            step = 2
        # Display 1 out of 3 labels on the x-axis.
        self.c.xAxis().setLabelStep(int(step))
        log.debug("step:" + str(step))

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
    
    def __datafact__(self, l1, labs, ulab, alert=False):
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
                    if r.valuei >= self.max_value and alert:
                        self.max_value = r.valuei
                    
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
