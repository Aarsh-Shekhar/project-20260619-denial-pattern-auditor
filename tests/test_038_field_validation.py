import unittest

from denial_pattern_auditor.models import Record
from denial_pattern_auditor.scoring import score_record


class DepthCheck38(unittest.TestCase):
    def test_038_field_validation(self):
        record = Record(id="denial-038", exposure=84789, signal=0.828, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
