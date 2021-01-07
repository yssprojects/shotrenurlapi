from os import environ
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

gplinkapi = environ.get('gplink')
shrinkme = environ.get('shirnkme')
shrinkearn = environ.get('hrinkearn')
urlshortx = environ.get('urlshortx')
 
@app.route("/")
def home():
    return render_template("main.html")

@app.route('/shrinkme',methods=['GET','POST'])
def id():
    w = request.args.get('url')
    base_url = f"https://shrinkme.io/api?api="+shrinkme+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    return data['shortenedUrl']
    
@app.route('/gplink',methods=['GET','POST'])
def ids():
    w = request.args.get('url')
    base_url = f"https://gplinks.in/api?api="+gplinkapi+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    return data['shortenedUrl']
  
@app.route('/shrinkearn',methods=['GET','POST'])
def ids():
    w = request.args.get('url')
    base_url = f"https://shrinkearn.com/api?api="+shrinkearn+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    return data['shortenedUrl']

@app.route('/urlshortx',methods=['GET','POST'])
def ida():
    w = request.args.get('url')
    base_url = f"https://urlshortx.com/api?api="+shrinkme+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    return data['shortenedUrl']

@app.errorhandler(404) 
def error():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port= 5000)
