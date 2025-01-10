import unittest
from src.sourcecode import EmailContentAnalyzer  # Corrected import path

class TestEmailContentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = EmailContentAnalyzer()

    def test_extract_information(self):
        # Extract sender, recipient, and subject from email content
        email_content = "Subject: Congratulations! You've won a lottery!"
        info = self.analyzer.extract_information(
            'sender@example.com', 'recipient@example.com', email_content
        )
        self.assertEqual(info['sender'], 'sender@example.com')
        self.assertEqual(info['recipient'], 'recipient@example.com')
        self.assertEqual(info['subject'], 'Congratulations! You\'ve won a lottery!')

    def test_identify_suspicious_content(self):
        # Verify detection of suspicious content
        suspicious_email = "You have been compromised. Your password is at risk."
        normal_email = "Hello, how are you?"
        self.assertTrue(self.analyzer.identify_suspicious_content(suspicious_email))
        self.assertFalse(self.analyzer.identify_suspicious_content(normal_email))

if __name__ == '__main__':
    unittest.main()
