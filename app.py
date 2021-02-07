from os import environ
from flask import Flask, render_template, request
import requests
import pyshorteners

app = Flask(__name__)

gplinkapi = environ.get('gplinkapi')
shrinkme = environ.get('shirnkmeapi')
shrinkearn = environ.get('shrinkearn')
zagl = environ.get('zagl')
exeio = environ.get('exeio')
 
@app.route("/")
def home():
    return "api Working"

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
def idss():
    w = request.args.get('url')
    base_url = f"https://shrinkearn.com/api?api="+shrinkearn+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    return data['shortenedUrl']

@app.route('/za.gl',methods=['GET','POST'])
def zo():
    w = request.args.get('url')
    base_url = f"https://za.gl/api?api="+zagl+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    return data['shortenedUrl']
  
@app.route('/exe.io',methods=['GET','POST'])
def exeio():
    w = request.args.get('url')
    base_url = f"https://exe.io/api?api="+exeio+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    return data['shortenedUrl']
   
@app.route('/bit.ly',methods=['GET','POST'])
def bitly():
    
    w = request.args.get('url')
    s = pyshorteners.Shortener(api_key='2304c97d78eeb8f011bfa4fbc704461986fc8162')
    shortened_url = s.bitly.shot(w)
    return shortened_url

@app.route('/da.gd',methods=['GET','POST'])
def dagd():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.dagd.short(w)
    return shortened_url


@app.errorhandler(404) 
def error():
    return "error"

if __name__ == "__main__":
     app.run(host="0.0.0.0",port= 5000)
