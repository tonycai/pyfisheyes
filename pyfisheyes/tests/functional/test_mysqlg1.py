from pyfisheyes.tests import *

class TestMysqlg1Controller(TestController):

    def test_index(self):
        response = self.app.get(url(controller='mysqlg1', action='index'))
        # Test response...
