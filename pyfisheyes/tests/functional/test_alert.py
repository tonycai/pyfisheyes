from pyfisheyes.tests import *

class TestAlertController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='alert', action='index'))
        # Test response...
