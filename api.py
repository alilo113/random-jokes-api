import random
import requests
from flask import Flask, jsonify
from bs4 import BeautifulSoup

jokes = []
url = "https://www.cultureamp.com/blog/funny-jokes-for-the-workplace"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('span', class_='text')

    for quote in quotes:
        jokes.append(quote.get_text())

app = Flask(__name__)

@app.route("/random")
def first_app():
    random_joke = random.choice(jokes)
    return jsonify({"joke": random_joke})

if __name__ == "__main__":
    app.run(debug=True) 