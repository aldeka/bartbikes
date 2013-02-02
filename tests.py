import unittest
import datetime
import app


class TestBartSchedule(unittest.TestCase):
    def test_weekend(self):
        d = datetime.datetime(year=2013, month=2, day=2, hour=8)
        answer = app.bart_schedule(current_time=d)['answer']
        self.assertTrue(answer == 'YES')
        
    def test_late_night(self):
        d = datetime.datetime(year=2013, month=2, day=1, hour=11)
        answer = app.bart_schedule(current_time=d)['answer']
        self.assertTrue(answer == 'YES')
        
    def test_morning_commute(self):
        d = datetime.datetime(year=2013, month=2, day=1, hour=8)
        answer = app.bart_schedule(current_time=d)['answer']
        self.assertTrue(answer == 'NO')
        
    def test_evening_commute(self):
        d = datetime.datetime(year=2013, month=2, day=1, hour=17, minute=30)
        answer = app.bart_schedule(current_time=d)['answer']
        self.assertTrue(answer == 'NO')
        
if __name__ == '__main__':
    unittest.main()
