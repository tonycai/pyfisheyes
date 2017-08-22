from pyfisheyes.tests import *

class TestSecurityController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='security', action='index'))
        # Test response...
