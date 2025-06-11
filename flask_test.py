from flask import Flask, jsonify, request
from textblob import TextBlob
import os



app = Flask(__name__)

@app.route('/analyse', methods=['GET','POST'])
def analyse():

    statement = request.json.get('statement')
    data = TextBlob(statement)
    sentiment = data.sentiment
    polarity = sentiment.polarity
    subjectivity = sentiment.subjectivity
    return jsonify({
        'polarity': polarity,
        'subjectivity': subjectivity
    })

@app.route('/ping')
def ping():
    return 'pong', 200

    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0', port=port)