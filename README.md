# Auto-Tweet-Generator
This Flask-based application generates and posts tweets automatically using OpenAI's language model and the X API. It takes a prompt as input and generates a specified number of tweets per day for a given number of days. The generated tweets are then posted to the connected Twitter account.

# Usage:

- Install the required dependencies using pip install -r requirements.txt.
- Run the Flask application using python app.py.
- Send a POST request to /generate-tweet endpoint with the following JSON payload:

{

    "prompt": "Your prompt text here",
    "quantity_per_day": 5,    // Number of tweets to generate per day
    "days": 7                 // Number of days to generate tweets for
    
}

- The application will generate the specified number of tweets per day based on the provided prompt and post them to the linked X account.

- Note: Ensure that the necessary API keys are securely configured and kept confidential.

# Dependencies:

- Flask
- Flask-CORS
- OpenAI
- Tweepy
# API Keys:

- OpenAI API Key
- X API Key (Consumer Key, Consumer Secret, Access Token, Access Token Secret)

# Contributing:
Contributions are welcome! Feel free to open an issue or submit a pull request.

# License:
This project is licensed under the MIT License.
