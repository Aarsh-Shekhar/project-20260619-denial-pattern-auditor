import unittest

from denial_pattern_auditor.models import Record
from denial_pattern_auditor.scoring import score_record


class DepthCheck50(unittest.TestCase):
    def test_050_threshold_calibration(self):
        record = Record(id="denial-050", exposure=88064, signal=0.402, urgency=1)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
