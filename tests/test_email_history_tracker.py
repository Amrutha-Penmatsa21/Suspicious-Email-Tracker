import unittest
from src.sourcecode import EmailHistoryTracker  # Corrected import path

class TestEmailHistoryTracker(unittest.TestCase):

    def setUp(self):
        self.history_tracker = EmailHistoryTracker()

    def test_add_email_history(self):
        # Add a history record and verify it is stored correctly
        self.history_tracker.add_email_history(
            'sender@example.com', 'recipient@example.com', 'Test email content', 75.0
        )
        history = self.history_tracker.get_email_history()
        self.assertEqual(len(history), 1)
        self.assertEqual(history[0]['sender'], 'sender@example.com')

    def test_sort_by_date(self):
        # Add multiple history records and sort by date
        self.history_tracker.add_email_history('sender@example.com', 'recipient@example.com', 'Test 1', 75.0)
        self.history_tracker.add_email_history('sender@example.com', 'recipient@example.com', 'Test 2', 85.0)
        self.history_tracker.sort_history(by='date')
        self.assertTrue(self.history_tracker.get_email_history()[0]['date'] > self.history_tracker.get_email_history()[1]['date'])

    def test_sort_by_suspicion(self):
        # Add multiple history records and sort by suspicion level
        self.history_tracker.add_email_history('sender@example.com', 'recipient@example.com', 'Test 1', 75.0)
        self.history_tracker.add_email_history('sender@example.com', 'recipient@example.com', 'Test 2', 85.0)
        self.history_tracker.sort_history(by='suspicion')
        self.assertTrue(self.history_tracker.get_email_history()[0]['suspicion_level'] > self.history_tracker.get_email_history()[1]['suspicion_level'])

if __name__ == '__main__':
    unittest.main()
