from flask import Flask,render_template,request
from pyshorteners import *
app=Flask(__name__)
@app.route("/")
def home():
	return render_template("home.html")

@app.route("/shorten",methods=["POST"])
def shorten():
	try:
		url=request.form["url"]
		s=Shortener()
		res=s.tinyurl.short(url.strip())
		return render_template("home.html",msg=res)
	except Exception as e:
		return render_template("home.html",msg="invalid url, please check it")
if __name__=="__main__":
	app.run(debug=True,use_reloader=True)