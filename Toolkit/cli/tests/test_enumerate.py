from __future__ import annotations

import json
import unittest
from pathlib import Path

from workflow_review.enumerate import enumerate_workflows


FIXTURE_PATH = Path(__file__).parent / "fixtures" / "sample_workflow.json"


class EnumerateWorkflowTests(unittest.TestCase):
    def test_enumerates_parent_and_embedded_workflows(self) -> None:
        result = enumerate_workflows(FIXTURE_PATH)
        self.assertEqual(result["workflow_count"], 2)
        self.assertEqual(result["parent_count"], 1)
        self.assertEqual(result["embedded_count"], 1)
        self.assertEqual(result["workflows"][0]["workflow_type"], "parent")
        self.assertEqual(result["workflows"][1]["workflow_type"], "embedded")

    def test_fixture_is_valid_json(self) -> None:
        data = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
        self.assertIn("workflow", data)


if __name__ == "__main__":
    unittest.main()
