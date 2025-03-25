from flask import Flask, request
from telegram import Bot
import config

app = Flask(__name__)
TOKEN = config.get_token()
bot = Bot(token=TOKEN)

@app.route('/', methods=["POST"])
def main():
    data = request.get_json()

    print(data)

    
    return data

@app.route('/home')
def home():
    return "Hello world"

if __name__ == '__main__':
    app.run(port=8080, debug=True)