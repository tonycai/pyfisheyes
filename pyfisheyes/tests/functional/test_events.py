from pyfisheyes.tests import *

class TestEventsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='events', action='index'))
        # Test response...
