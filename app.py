import requests
from flask import Flask

app = Flask(__name__)


@app.route('/search/<string:name>', methods=['POST'])
def search(name):
    location = '/api/search/suggest/web'
    location += '?s=%s&limit=30&offset=0&type=1' % name    # set search params

    return fetch('POST', location)


@app.route('/songs/<int:song_id>', methods=['GET'])
def songs(song_id):

    location = '/api/song/detail?ids=%5B{0}%5d'.format(song_id)

    return fetch('GET', location)


@app.route('/lyrc/<int:lyrc_id>', methods=['GET'])
def lyrc(lyrc_id):

    location = '/api/song/lyric?lv={0}&id={1}'.format(song_id, -1)

    return fetch('GET', location)


def fetch(method, location):
    origin = 'http://music.163.com'
    url = origin + location

    headers = {'Origin': origin, 'Referer': origin, 'Accept': 'application/json', 'Content-Type': 'application/json'}

    if method == 'GET':
        req = requests.get(url, headers=headers)
    elif method == 'POST':
        req = requests.post(url, headers=headers)

    print '>', url
    return req.text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
