import unittest
from src.sourcecode import SuspicionCalculator  # Corrected import path

class TestSuspicionCalculator(unittest.TestCase):

    def setUp(self):
        self.keyword_weights = {
            "urgent": 5,
            "lottery": 10,
            "password": 8,
            "compromised": 7
        }
        self.calculator = SuspicionCalculator(self.keyword_weights)

    def test_calculate_suspicion(self):
        email_content = "This is an urgent email with a password reset request."
        suspicion = self.calculator.calculate_suspicion(email_content)
        self.assertGreater(suspicion, 0)

    def test_no_suspicion(self):
        email_content = "Hello, this is just a normal email."
        suspicion = self.calculator.calculate_suspicion(email_content)
        self.assertEqual(suspicion, 0)

if __name__ == '__main__':
    unittest.main()
