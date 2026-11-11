"""Regression checks for published tournament guide metadata."""
import unittest
from pathlib import Path
import yaml


class TournamentMetadataTest(unittest.TestCase):
    def test_description_meets_agents_character_limit(self):
        guide = Path(__file__).resolve().parents[1] / 'guides/tournament-creation.md'
        front = yaml.safe_load(guide.read_text(encoding='utf-8').split('---', 2)[1])
        description = front['description']
        self.assertGreaterEqual(len(description), 140)
        self.assertLessEqual(len(description), 160)
        self.assertIn('group stages', description)
        self.assertEqual(front['permalink'], '/guides/tournament-creation/')


if __name__ == '__main__':
    unittest.main()
