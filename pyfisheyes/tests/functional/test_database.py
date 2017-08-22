from pyfisheyes.tests import *

class TestDatabaseController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='database', action='index'))
        # Test response...
