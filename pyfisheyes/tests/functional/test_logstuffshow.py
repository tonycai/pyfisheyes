from pyfisheyes.tests import *

class TestLogstuffshowController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='logstuffshow', action='index'))
        # Test response...
