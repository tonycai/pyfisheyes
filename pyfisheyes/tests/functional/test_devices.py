from pyfisheyes.tests import *

class TestDevicesController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='devices', action='index'))
        # Test response...
