import slack

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def forward():
    request.get_data()
    body = request.form['Body']
    slack.post(body)
    return ""
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
