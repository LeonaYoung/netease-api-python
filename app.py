import requests
from flask import Flask

app = Flask(__name__)


@app.route('/search/<string:name>', methods=['POST'])
def index(name):
    origin = 'http://music.163.com'
    url = origin + '/api/search/suggest/web'
    url += '?s=%s&limit=30&offset=0&type=1' % name    # set search params

    headers = {'Origin': origin, 'Referer': origin, 'Accept': 'application/json', 'Content-Type': 'application/json'}

    req = requests.post(url, headers=headers)

    print '>', url
    return req.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
