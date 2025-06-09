from flask import Flask, jsonify, request
from textblob import TextBlob



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