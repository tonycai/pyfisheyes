from pyfisheyes.tests import *

class TestCookieController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='cookie', action='index'))
        # Test response...
