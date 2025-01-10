import unittest
from src.sourcecode import KeywordWeights  # Corrected import path

class TestKeywordWeights(unittest.TestCase):

    def setUp(self):
        self.kw = KeywordWeights()
        self.kw.add_weight("lottery", 10)
        self.kw.add_weight("urgent", 5)

    def test_load_weights(self):
        # Add new keyword and verify it is added correctly
        self.kw.add_weight("bank", 6)
        self.assertEqual(self.kw.get_weight("bank"), 6)

    def test_update_weight(self):
        # Update existing keyword weight and verify the update
        self.kw.update_weight("urgent", 7)
        self.assertEqual(self.kw.get_weight("urgent"), 7)

    def test_get_weight(self):
        # Check if weights are returned correctly
        self.assertEqual(self.kw.get_weight("lottery"), 10)
        self.assertEqual(self.kw.get_weight("unknown"), 0)

if __name__ == '__main__':
    unittest.main()
