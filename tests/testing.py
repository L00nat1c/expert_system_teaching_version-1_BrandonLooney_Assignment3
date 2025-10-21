import unittest
from engine import Rule, ForwardChainingEngine
from kb_loader import load_rules

KB_PATH = "kb/laptop_rules.json"

class TestLaptopExpertSystem(unittest.TestCase):

    # Set up the engine with rules before each test
    def setUp(self):
        self.rules = load_rules(KB_PATH)
        self.engine = ForwardChainingEngine(self.rules)

    # Helper function to run the engine with given facts
    def run_engine(self, facts):
        """Helper function to run the engine and return recommendations."""
        self.engine.assert_facts(facts)
        self.engine.run()
        results = self.engine.conclusions()
        return results["recommendations"]

    # Test cases for various scenarios
    # Premmium Ultrabook Test
    def test_premium_ultrabook(self):
        """budget_high + portable + long_battery → premium_ultrabook"""
        facts = ["budget_high", "portable", "long_battery"]
        recs = self.run_engine(facts)
        self.assertIn("premium_ultrabook", recs)

    # Budget Ultrabook Test
    def test_budget_ultrabook(self):
        """budget_low + portable + office_only → budget_ultrabook"""
        facts = ["budget_low", "portable", "office_only"]
        recs = self.run_engine(facts)
        self.assertIn("budget_ultrabook", recs)

    # Midrange Gaming Test
    def test_midrange_gaming(self):
        """budget_medium + gaming → midrange_gaming_laptop"""
        facts = ["budget_medium", "gaming"]
        recs = self.run_engine(facts)
        self.assertIn("midrange_gaming_laptop", recs)

    # Highend Gaming Test
    def test_highend_gaming(self):
        """budget_high + gaming → highend_gaming_laptop"""
        facts = ["budget_high", "gaming"]
        recs = self.run_engine(facts)
        self.assertIn("highend_gaming_laptop", recs)

    # Linux Friendly Hardware Test
    def test_linux_friendly(self):
        """pref_os_linux + office_only → spec:linux_friendly_hw"""
        facts = ["pref_os_linux", "office_only"]
        self.engine.assert_facts(facts)
        self.engine.run()
        results = self.engine.conclusions()
        self.assertIn("linux_friendly_hw", results["specs"])

if __name__ == "__main__":
    unittest.main()
