import unittest
from models.charity import Charity

class TestCharity(unittest.TestCase):
    
    def setUp(self):
        self.charity = Charity("Mind", "Support to anyone experiencing a mental health problem", "www.mind.org.uk")
    
    def test_charity_has_name(self):
        self.assertEqual("Mind", self.charity.name)
    
    def test_charity_has_description(self):
        self.assertEqual("Support to anyone experiencing a mental health problem", self.charity.description)

    def test_charity_has_website(self):
        self.assertEqual("www.mind.org.uk", self.charity.website)