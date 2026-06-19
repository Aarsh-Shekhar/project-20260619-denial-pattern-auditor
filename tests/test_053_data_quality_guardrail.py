import unittest

from denial_pattern_auditor.models import Record
from denial_pattern_auditor.scoring import score_record


class DepthCheck53(unittest.TestCase):
    def test_053_data_quality_guardrail(self):
        record = Record(id="denial-053", exposure=47764, signal=0.415, urgency=4)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
