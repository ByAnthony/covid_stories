import unittest
from models.contributor import Contributor

class TestContributor(unittest.TestCase):

    def setUp(self):
        self.contributor = Contributor("Anthony", "Byledbal", 35, "CodeClan Student", "Glasgow")

    def test_contributor_has_first_name(self):
        self.assertEqual("Anthony", self.contributor.first_name)

    def test_contributor_has_last_name(self):
        self.assertEqual("Byledbal", self.contributor.last_name)

    def test_contributor_has_age(self):
        self.assertEqual(35, self.contributor.age)

    def test_contributor_has_profession(self):
        self.assertEqual("CodeClan Student", self.contributor.profession)

    def test_contributor_has_address(self):
        self.assertEqual("Glasgow", self.contributor.address)