###  `USAGE.md`**

```markdown
# Usage Guide

## 1. Running the Program

    After you have set up the project as described in `INSTALLATION.md`, run the main program script to start the email analysis:

    ```bash
    python suspiciousemailtracker/src/sourcecode.py
     The program will prompt you to enter the email details manually:
## 2. Enter Email Details
     Sender's Email: Enter the email address of the sender.
     Recipient's Email: Enter the email address of the recipient.

  Example Console Interaction:
     Email Content: Enter the full content of the email (including the subject line).
     Enter the sender's email address: sender@example.com
     Enter the recipient's email address: recipient@example.com
     Please enter the email content: Congratulations! You have won a lottery.

## 3. View Analysis Results
     The program will process the email content, extract relevant information, and calculate a suspicion level. It will display the following information:

     Extracted Information: The program will identify the sender, recipient, and subject of the email.
     Suspicion Level: A percentage score indicating the suspicion level of the email based on the occurrence of predefined keywords.
  Example Output:

     Extracted Information:
     {'sender': 'sender@example.com', 'recipient': 'recipient@example.com', 'subject': 'Congratulations!'}

     Suspicion Level:
     72.73%
## 4. Email History
     Processed email details (including suspicion level and timestamp) will be stored in the email_history.json file for future reference.

     To view the email history, simply check the contents of the data/email_history.json file. It will contain entries in the following format:
      
     [
       {
          "sender": "sender@example.com",
          "recipient": "recipient@example.com",
          "content": "congratulations you have won a lottery",
          "suspicion_level": 72.73,
          "date": "2025-01-09 10:00:00"
        }
      ]


