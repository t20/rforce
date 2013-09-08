import requests
import json

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

READYFORCE_MEMBER_SEARCH_URL = "http://www.readyforce.com/api/v1/member_search"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    q = request.args.get('q', '')
    limit = request.args.get('limit', 10)
    res = get_readyforce_data(q, limit)
    return json.dumps(res)


def get_readyforce_data(q, limit=10):
    if not q:
        return []
    params = {"search": q, "limit": limit, "verbosity": "verbose"}
    response = requests.post(READYFORCE_MEMBER_SEARCH_URL, data=json.dumps(params))
    # print 'Got response back', response.status_code
    if response.status_code != 200:
        return []
    response = json.loads(response.text)
    if response.get('errors', []):
        return []
    result = response.get('result', {})
    members = result.get('members', [])
    return members


if __name__ == '__main__':
    #app.debug = True
    app.run()
