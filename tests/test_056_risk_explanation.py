import unittest

from denial_pattern_auditor.models import Record
from denial_pattern_auditor.scoring import score_record


class DepthCheck56(unittest.TestCase):
    def test_056_risk_explanation(self):
        record = Record(id="denial-056", exposure=38793, signal=0.885, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
