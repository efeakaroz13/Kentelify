from flask import Flask,render_template,request,redirect
from flask_cors import CORS 
from kauth import kauth 


auth = kauth("Kentelify")
app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
	return render_template("base.html")

@app.route("/register",methods=["POST","GET"])
def register():
	msg = request.args.get("msg")
	if msg!=None:
		if msg == "noscc":
			return render_template("register.html",error=True)

	if request.method == "POST":
		username =request.form.get("username")
		password = request.form.get("password")
		fullname = request.form.get("fullname")
		response = auth.createuser(username=username,password=password,fullname=fullname)
		if response["SCC"] == True:
			return redirect("/login?msg=scc")
		if response["SCC"] == False:
			return redirect("/register?msg=noscc")
	return render_template("register.html")

@app.route("/login")
def login():
	return render_template("login.html")

if __name__ == "__main__":
	app.run(debug=True)
