from flask import Flask, request, jsonify
import openai
import tweepy
import os

from flask_cors import CORS, cross_origin

# OpenAI API setup
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Twitter API setup
client = tweepy.Client(
    consumer_key=os.environ.get('TWITTER_CONSUMER_KEY'),
    consumer_secret=os.environ.get('TWITTER_CONSUMER_SECRET'),
    access_token=os.environ.get('TWITTER_ACCESS_TOKEN'),
    access_token_secret=os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
)

app = Flask(__name__)

cors = CORS(app)

def generate_tweet(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=50
    )
    return response.choices[0].text.strip()

def post_tweet(tweet):
    client.create_tweet(text=tweet)

@app.route("/generate-tweet", methods=["POST"])
def generate_tweet_api():
    prompt = request.json["prompt"]
    quantity_per_day = int(request.json["quantity_per_day"])
    days = int(request.json["days"])

    tweets = []
    for _ in range(quantity_per_day * days):
        tweet = generate_tweet(prompt)
        tweets.append(tweet)

    for tweet in tweets:
        post_tweet(tweet)

    return jsonify({"tweets": tweets})

if __name__ == "__main__":
    app.run(debug=True)
