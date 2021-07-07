import unittest
import datetime
from myghub.dt.timemachine import TimeMachine


class TestTimeMachine(unittest.TestCase):
    def setUp(self):
        self.timemachine = TimeMachine()

    def test_str_to_dt_with_default_format(self):
        dt = self.timemachine.str_to_dt('2021-07-07 12:31:59')
        self.assertIsInstance(dt, datetime.datetime)
        self.assertEqual(dt.year, 2021)
        self.assertEqual(dt.month, 7)
        self.assertEqual(dt.day, 7)
        self.assertEqual(dt.hour, 12)
        self.assertEqual(dt.minute, 31)
        self.assertEqual(dt.second, 59)

    def test_str_to_dt_with_utcdatetime_format(self):
        dt = self.timemachine.str_to_dt('2021-07-07T12:31:59', '%Y-%m-%dT%H:%M:%S')
        self.assertIsInstance(dt, datetime.datetime)
        self.assertEqual(dt.year, 2021)
        self.assertEqual(dt.month, 7)
        self.assertEqual(dt.day, 7)
        self.assertEqual(dt.hour, 12)
        self.assertEqual(dt.minute, 31)
        self.assertEqual(dt.second, 59)

    def test_dt_to_str_with_default_format(self):
        dt = self.timemachine.str_to_dt('2021-07-07 12:31:59')
        sdt = self.timemachine.dt_to_str(dt)
        self.assertIsInstance(sdt, str)
        self.assertNotIsInstance(sdt, datetime.datetime)
        self.assertEqual(sdt, '2021-07-07 12:31:59')

    def test_dt_to_str_with_utcdate_format(self):
        dt = self.timemachine.str_to_dt('2021-07-07 12:31:59')
        sdt = self.timemachine.dt_to_str(dt, '%Y-%m-%dT%H:%M:%S')
        self.assertIsInstance(sdt, str)
        self.assertNotIsInstance(sdt, datetime.datetime)
        self.assertEqual(sdt, '2021-07-07T12:31:59')


if __name__ == '__main__':
    unittest.main()
