import unittest
from models.memory import Memory

class TestMemory(unittest.TestCase):

    def setUp(self):
        self.memory = Memory("Lacking Nature", 1, "My Story of lockdown", "2021-09-25", 2)

    def test_memory_has_title(self):
        self.assertEqual("Lacking Nature", self.memory.title)

    def test_memory_has_contributor_id(self):
        self.assertEqual(1, self.memory.contributor)

    def test_memory_has_story(self):
        self.assertEqual("My Story of lockdown", self.memory.story)
    
    def test_memory_has_date(self):
        self.assertEqual("2021-09-25", self.memory.date)

    def test_memory_has_charity_id(self):
        self.assertEqual(2, self.memory.charity)