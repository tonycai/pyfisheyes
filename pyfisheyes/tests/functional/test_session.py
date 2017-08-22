from pyfisheyes.tests import *

class TestSessionController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='session', action='index'))
        # Test response...
