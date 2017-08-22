from pyfisheyes.tests import *

class TestWsgiappController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='wsgiapp', action='index'))
        # Test response...
