from flask import Flask, request

app = Flask(__name__)
@app.route('/')
def main():
    return "Hello GitHub"

@app.route('/get/sum')
def get_sum():
    query = request.args
    a = query.get('a', 0)
    b = query.get('b', 0)
    return {"sum" : int(a) + int(b)}

if __name__ == "__main__":
    app.run(debug=True)