from flask import Flask, render_template, request
import requests
import pyshorteners

app = Flask(__name__)

gplinkapi = "714d94cc0bee820944c8007db0f684d40e29fe27"
shrinkme = "9b8aab2630a0e5c289837488ea83536e6912dd99"
shrinkearn = "4fc97cae14f38321754a8adcdd85d466636ced83"
zagl = "db128276207f992dc588eb8dece54de4cde2c663"
exeio = "35ea7ecf4e3d29cbfee7ddbc9701f58e95602452"
 
@app.route("/")
def home():
    return "hi"

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
def idaas():
    w = request.args.get('url')
    base_url = f"https://za.gl/api?api="+zagl+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    return data['shortenedUrl']
  
@app.route('/exe.io',methods=['GET','POST'])
def isds():
    w = request.args.get('url')
    base_url = f"https://exe.io/api?api="+exeio+"&url="+(w)
    torrent_results = requests.get(url=base_url).json()
    data = torrent_results
    return data['shortenedUrl']

@app.route('/da.gd',methods=['GET','POST'])
def iaads():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.dagd.short(w)
    return shortened_url

@app.errorhandler(404) 
def error():
    return "error"

if __name__ == "__main__":
    app.run()
