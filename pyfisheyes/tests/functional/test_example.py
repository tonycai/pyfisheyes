from pyfisheyes.tests import *

class TestExampleController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='example', action='index'))
        # Test response...
