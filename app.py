from flask import Flask, request, jsonify
from flask_cors import CORS


from src.sourcecode import EmailScanner, SuspicionCalculator, KeywordWeights

app = Flask(__name__)
CORS(app)

# Load keyword weights
keyword_weights = KeywordWeights()
keyword_weights.load_weights('data/keyword_weights.json')

@app.route('/process_email', methods=['POST'])
def process_email():
    data = request.json
    email_scanner = EmailScanner()
    email_scanner.sender = data['sender']
    email_scanner.recipient = data['recipient']
    email_scanner.email_content = data['content']
    email_scanner.preprocess_email()

    calculator = SuspicionCalculator(keyword_weights.weights)
    suspicion_level = calculator.calculate_suspicion(email_scanner.email_content)

    return jsonify({'suspicion_level': suspicion_level})

if __name__ == '__main__':
    app.run(debug=True)
