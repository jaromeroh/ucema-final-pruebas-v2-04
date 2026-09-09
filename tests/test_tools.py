import unittest
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from tools import get_data

class ToolTests(unittest.TestCase):
    def test_adjacent_meeting_does_not_conflict(self):
        self.assertEqual(get_data(ROOT,'01')['slots'][0]['start'],'2026-09-10T09:30:00+00:00')
    def test_no_common_availability(self):
        self.assertEqual(get_data(ROOT,'02')['slots'],[])
    def test_full_duration_fits(self):
        slots=get_data(ROOT,'03')['slots']
        self.assertEqual(slots,[{'start':'2026-09-10T13:30:00+00:00','end':'2026-09-10T14:30:00+00:00'},
                               {'start':'2026-09-10T14:00:00+00:00','end':'2026-09-10T15:00:00+00:00'}])

if __name__ == "__main__": unittest.main()
