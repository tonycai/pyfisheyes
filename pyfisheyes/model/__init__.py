"""The application's model objects"""
from pyfisheyes.model.meta import Session, Base

from pyfisheyes.model.fisheyesdb.categories import Categories
from pyfisheyes.model.fisheyesdb.graphs import Graphs
from pyfisheyes.model.fisheyesdb.graphshour import GraphsHour
from pyfisheyes.model.fisheyesdb.graphshost import GraphsHost
from pyfisheyes.model.fisheyesdb.events import Events
from pyfisheyes.model.fisheyesdb.users import Users
from pyfisheyes.model.fisheyesdb.contacts import Contacts
from pyfisheyes.model.fisheyesdb.realtime import Realtime
from pyfisheyes.model.fisheyesdb.logstuff import Logstuff
from pyfisheyes.model.fisheyesdb.alarminfo import Alarminfo
from pyfisheyes.model.fisheyesdb.dateitems import Dateitems
from pyfisheyes.model.fisheyesdb.img_event import ImgEvent
from pyfisheyes.model.fisheyesdb.messages import Messages
from pyfisheyes.model.fisheyesdb.devices import Devices,V_Devices
from pyfisheyes.model.fisheyesdb.chartstyle import ChartStyle
from pyfisheyes.model.fisheyesdb.devicebase import DeviceBase
from pyfisheyes.model.fisheyesdb.deviceitemsets import DeviceItemSets
from pyfisheyes.model.fisheyesdb.deviceitemgroup import DeviceItemGroup
#from pyfisheyes.model.fisheyesdb.devices_realtime import DevicesRealtime
#from pyfisheyes.model.fisheyesdb.device_item_sets import DeviceItemSets
def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
