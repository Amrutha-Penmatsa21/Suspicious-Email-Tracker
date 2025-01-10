# Suspicious Email Tracker

## Overview
The **Suspicious Email Tracker** is a Python-based application that helps identify potentially suspicious or phishing emails by analyzing their content for specific keywords. It evaluates the suspicion level based on predefined keyword weights and provides the user with detailed results. This tool is especially useful in detecting scam emails.

## Features
- **Email Analysis**: Input email details (sender, recipient, content) and evaluate its suspicion level.
- **Keyword-based Evaluation**: Suspicion levels are calculated using predefined keyword weights.
- **Email History Tracking**: Tracks previously processed emails and stores them for future reference.
- **Customizable Keywords**: Modify keyword weights in `keyword_weights.json` to suit your needs.
  
## Project Structure
suspicious_email_tracker 
1. src\ sourcecode.py (main logic of the program)
2. data\sampleemails,email_history.json,keyword_weights.jspn  # Input/output files (keyword weights, email history)
3. docs\ # Documentation files (this folder) 
4. tests\ # Unit tests for the project

## Installation

See the `INSTALLATION.md` file for detailed setup instructions.

## Usage

For detailed usage instructions, refer to the `USAGE.md` file.

## Contributing

We welcome contributions! Please refer to the `CONTRIBUTING.md` file for guidelines on contributing.

## Changelog

Check the `CHANGELOG.md` for updates and changes to the project.



