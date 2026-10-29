import json
import unittest
from pathlib import Path
from main import analyze

class SampleDataTests(unittest.TestCase):
    def test_sample_dataset_has_five_examples_and_required_fields(self):
        path = Path(__file__).resolve().parents[1] / "sample_tickets.json"
        examples = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(len(examples), 5)
        for item in examples:
            self.assertTrue(item["id"])
            self.assertTrue(item["ticket"].strip())
            self.assertTrue(item["category_expected"])

    def test_empty_input_is_rejected_without_api_call(self):
        with self.assertRaises(ValueError):
            analyze("  ")

if __name__ == "__main__":
    unittest.main()
