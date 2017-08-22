from pyfisheyes.tests import *

class TestApperrorlogController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='apperrorlog', action='index'))
        # Test response...
