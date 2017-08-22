from pyfisheyes.tests import *

class TestDailyReportController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='daily_report', action='index'))
        # Test response...
