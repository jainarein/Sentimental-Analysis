from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  # Allow requests from your frontend

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data['text']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = 'Positive 😊'
    elif polarity < 0:
        sentiment = 'Negative 😠'
    else:
        sentiment = 'Neutral 😐'

    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
