from pyfisheyes.tests import *

class TestTmcController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='tmc', action='index'))
        # Test response...
