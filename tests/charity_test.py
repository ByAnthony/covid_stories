import unittest
from models.charity import Charity

class TestCharity(unittest.TestCase):
    
    def setUp(self):
        self.charity = Charity("Mind", "Support to anyone experiencing a mental health problem", "www.mind.org.uk", "/static/images/logo/mind.png")
    
    def test_charity_has_name(self):
        self.assertEqual("Mind", self.charity.name)
    
    def test_charity_has_description(self):
        self.assertEqual("Support to anyone experiencing a mental health problem", self.charity.description)

    def test_charity_has_website(self):
        self.assertEqual("www.mind.org.uk", self.charity.website)

    def test_charity_has_image(self):
        self.assertEqual("/static/images/logo/mind.png", self.charity.image)