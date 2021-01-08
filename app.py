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
@app.route('/bit.ly',methods=['GET','POST'])
def iaaads():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.bitly.short(w)
    return shortened_url
 
@app.route('/chilp.it',methods=['GET','POST'])
def iaqads():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.chilpit.short(w)
    return shortened_url

@app.route('/clck.ru',methods=['GET','POST'])
def iaqds():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.clckru.short(w)
    return shortened_url

@app.route('/cutt.ly',methods=['GET','POST'])
def iazads():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.cutt.ly.short(w)
    return shortened_url

@app.route('/git.io',methods=['GET','POST'])
def iaads():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.git.io.short(w)
    return shortened_url

@app.route('/is.gd',methods=['GET','POST'])
def iaadas():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.isgd.short(w)
    return shortened_url

@app.route('/nullpointer',methods=['GET','POST'])
def iaazads():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.nullpointer.short(w)
    return shortened_url

@app.route('/os.db',methods=['GET','POST'])
def osdb():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.osdb.short(w)
    return shortened_url

@app.route('/ow.ly',methods=['GET','POST'])
def owly():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.owly.short(w)
    return shortened_url

@app.route('/po.st',methods=['GET','POST'])
def post():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.post.short(w)
    return shortened_url

@app.route('/qps.ru',methods=['GET','POST'])
def qpsru():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.qpsru.short(w)
    return shortened_url

@app.route('/short.cm',methods=['GET','POST'])
def shortcm():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.shortcm.short(w)
    return shortened_url

@app.route('/tiny.cc',methods=['GET','POST'])
def tinycc():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.tinycc.short(w)
    return shortened_url

@app.route('/tinyurl.com',methods=['GET','POST'])
def tinyurl():
    w = request.args.get('url')
    s = pyshorteners.Shortener() 
    shortened_url = s.tinyurl.short(w)
    return shortened_url

@app.errorhandler(404) 
def error():
    return "error"

if __name__ == "__main__":
     app.run(host="0.0.0.0",port= 5000)
