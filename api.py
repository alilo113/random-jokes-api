import random
import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup

url = "https://www.cultureamp.com/blog/funny-jokes-for-the-workplace"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    jokes = soup.find_all('li')  # Assuming jokes are within <p> tags

    joke_texts = []
    for joke in jokes:
        text = joke.get_text()
        if text.strip():  # Check if the text content is not empty
            joke_texts.append(text)


app = Flask(__name__)

@app.route("/random")
def first_app():
    random_joke = random.choice(joke_texts)  # Use joke_texts instead of jokes
    return jsonify({"joke": random_joke})

if __name__ == "__main__":
    app.run(debug=True)