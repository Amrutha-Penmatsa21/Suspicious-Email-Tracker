import string
import re
import json
from datetime import datetime


class EmailScanner:
    def __init__(self):
        self.email_content = ""
        self.sender = ""
        self.recipient = ""
        
    def input_email(self):
        try:
            self.sender = input("Enter the sender's email address: ")
            while not re.match(r"[^@]+@[^@]+\.[^@]+", self.sender):
                print("Invalid email format. Please try again.")
                self.sender = input("Enter the sender's email address: ")

            self.recipient = input("Enter the recipient's email address: ")
            while not re.match(r"[^@]+@[^@]+\.[^@]+", self.recipient):
                print("Invalid email format. Please try again.")
                self.recipient = input("Enter the recipient's email address: ")

            self.email_content = input("Please enter the email content: ")
        except Exception as e:
            print("Error while reading email content:", e)
    
    def preprocess_email(self):
        self.email_content = self.email_content.lower()
        self.email_content = self.email_content.translate(str.maketrans('', '', string.punctuation))


class SuspicionCalculator:
    def __init__(self, keyword_weights):
        self.keyword_weights = keyword_weights
    
    def calculate_suspicion(self, email_content):
        total_weight = 0
        for keyword, weight in self.keyword_weights.items():
            if keyword in email_content:
                total_weight += weight
        
        max_possible_weight = sum(self.keyword_weights.values())
        suspicion_percentage = (total_weight / max_possible_weight) * 100 if max_possible_weight != 0 else 0
        return suspicion_percentage


class KeywordWeights:
    def __init__(self):
        self.weights = {}
    
    def load_weights(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.weights = json.load(file)
        except FileNotFoundError as e:
            print("File not found:", e)
    
    def add_weight(self, keyword, weight):
        self.weights[keyword] = weight
    
    def update_weight(self, keyword, weight):
        self.weights[keyword] = weight
    
    def get_weight(self, keyword):
        return self.weights.get(keyword, 0)


class EmailContentAnalyzer:
    def extract_information(self, sender, recipient, email_content):
        subject = re.search(r"Subject: (.+)", email_content)
        
        return {
            'sender': sender,
            'recipient': recipient,
            'subject': subject.group(1) if subject else "No Subject"
        }
    
    def identify_suspicious_content(self, email_content):
        return "suspicious" in email_content.lower()


class SuspiciousKeywordManager:
    def __init__(self):
        self.keywords = {}
    
    def add_keyword(self, keyword, weight):
        self.keywords[keyword] = weight
    
    def remove_keyword(self, keyword):
        if keyword in self.keywords:
            del self.keywords[keyword]
    
    def search_keyword(self, keyword):
        return keyword in self.keywords
    
    def update_keyword_weights(self, keyword, new_weight):
        if keyword in self.keywords:
            self.keywords[keyword] = new_weight


class EmailHistoryTracker:
    def __init__(self):
        self.history = []
    
    def add_email_history(self, sender, recipient, email_content, suspicion_level):
        date_scanned = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append({
            'sender': sender,
            'recipient': recipient,
            'content': email_content,
            'suspicion_level': suspicion_level,
            'date': date_scanned
        })
    
    def get_email_history(self):
        return self.history
    
    def sort_history(self, by='date'):
        if by == 'date':
            self.history.sort(key=lambda x: x['date'], reverse=True)
        elif by == 'suspicion':
            self.history.sort(key=lambda x: x['suspicion_level'], reverse=True)


# Example usage and output generation
if __name__ == "__main__":
    # Initialize components
    email_scanner = EmailScanner()
    keyword_manager = SuspiciousKeywordManager()
    history_tracker = EmailHistoryTracker()

    # Adding some sample keywords and weights
    keyword_manager.add_keyword("urgent", 5)
    keyword_manager.add_keyword("lottery", 10)
    keyword_manager.add_keyword("password", 8)

    # Input email details
    email_scanner.input_email()
    email_scanner.preprocess_email()

    calculator = SuspicionCalculator(keyword_manager.keywords)
    analyzer = EmailContentAnalyzer()

    # Analyze email
    extracted_info = analyzer.extract_information(
        email_scanner.sender, 
        email_scanner.recipient, 
        email_scanner.email_content
    )
    suspicion_level = calculator.calculate_suspicion(email_scanner.email_content)

    history_tracker.add_email_history(
        email_scanner.sender, 
        email_scanner.recipient, 
        email_scanner.email_content, 
        suspicion_level
    )

    # Display results
    print("\nExtracted Information:")
    print(extracted_info)

    print("\nSuspicion Level:")
    print(f"{suspicion_level:.2f}%")

    print("\nEmail History:")
    for record in history_tracker.get_email_history():
        print(record)
