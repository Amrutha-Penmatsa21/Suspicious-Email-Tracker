import unittest
from unittest.mock import patch
from src.sourcecode import EmailScanner  # Corrected import path

class TestEmailScanner(unittest.TestCase):

    @patch('builtins.input', side_effect=['sender@example.com', 'recipient@example.com', 'This is a test email.'])
    def test_input_email(self, mock_input):
        scanner = EmailScanner()
        scanner.input_email()
        
        # Verify all attributes were correctly set
        self.assertEqual(scanner.sender, 'sender@example.com')
        self.assertEqual(scanner.recipient, 'recipient@example.com')
        self.assertEqual(scanner.email_content, 'This is a test email.')

    @patch('builtins.input', side_effect=['invalid_email', 'recipient@example.com', 'This is a test email.'])
    def test_invalid_email_format(self, mock_input):
        scanner = EmailScanner()
        scanner.input_email()
        
        # Ensure invalid email input is handled
        self.assertNotEqual(scanner.sender, 'invalid_email')

if __name__ == '__main__':
    unittest.main()
