from flask import Flask
app = Flask(__name__)

@app.route('/now332')
def now332():
    import requests
    import json
    resp = requests.get('http://news.now.com/api/checkout?pid=webch332s&portal=news&service=NOWNEWS&type=channel').text
    json_obj = json.loads(resp)
    m3u8_url = json_obj['html5streamurl']
    proxies = {'http': "socks5://localhost:1111"}
    return requests.get(m3u8_url, proxies=proxies).content
app.run()
