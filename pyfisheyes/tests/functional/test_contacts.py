from pyfisheyes.tests import *

class TestContactsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='contacts', action='index'))
        # Test response...
