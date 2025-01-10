1. # Installation Guide

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Setup Steps

###  Clone the Repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/suspicious_email_tracker.git
2.   # Install Dependencies

  Navigate to the project directory and install the necessary dependencies:
       cd suspicious_email_tracker
       pip install -r requirements.txt


3. Set Up the Data Folder
    Ensure that the following files are created in the data/ folder:

     sample_emails.txt: Contains sample email content (optional).
     keyword_weights.json: A JSON file with keyword weights (default provided).
     email_history.json: Empty JSON file to track email analysis history (starts with an empty array []).

4.   Run the Program
       Execute the main script to start the program:


        python suspiciousemailtracker/src/sourcecode.py
       You can then interact with the application via the terminal to input email details (sender, recipient, content), and it will output the suspicion level and extracted information.

Optional: Running the UI
If you wish to use a graphical user interface (GUI), follow the instructions to set up the GUI framework. Refer to the project documentation on UI setup (to be implemented).

Troubleshooting
If you encounter issues related to missing modules, ensure all dependencies are installed via pip install -r requirements.txt.
For GUI-related issues, ensure you have the required libraries installed (e.g., Tkinter or PyQt5).     