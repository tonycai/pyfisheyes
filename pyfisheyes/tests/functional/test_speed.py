from pyfisheyes.tests import *

class TestSpeedController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='speed', action='index'))
        # Test response...
