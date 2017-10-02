from flask import Flask
app = Flask(__name__)

@app.route('/now332.m3u8')
def now332():
    import requests
    import json
    proxies = {
        'http': "socks5://localhost:1111",
        'https': "socks5://localhost:1111"
    }
    resp = requests.get('http://news.now.com/api/checkout?pid=webch332s&portal=news&service=NOWNEWS&type=channel', proxies=proxies).text
    json_obj = json.loads(resp)
    m3u8_url = json_obj['html5streamurl']
    content = requests.get(m3u8_url, proxies=proxies).content
    return content
if __name__ == '__main__':
    app.run('0.0.0.0')
