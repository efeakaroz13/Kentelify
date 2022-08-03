from flask import Flask,render_template,request,redirect,make_response
from flask_cors import CORS 
from kauth import kauth 
from cryptography.fernet import Fernet


key=b'D71kHIq7Wsyrjd30avvyzrS7BTT74lAXBB5y6mllnsQ='
fernet = Fernet(key)
def encrypt(text):
	encodedtext = fernet.encrypt(text.encode())
	return encodedtext.decode()
def decrypt(text):
	encodedtext = fernet.decrypt(text.encode())
	return encodedtext.decode()


auth = kauth("Kentelify")
app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
	username = request.cookies.get("username")
	password = request.cookies.get("password")
	if username == None or username.strip() =="":

		return render_template("base.html")
	else:
		username = decrypt(username)
		password = decrypt(request.cookies.get("password"))
		return render_template("home.html")

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

@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "POST":

		username = request.form.get("username")
		password = request.form.get("password")
		check = auth.login(username,password)
		if check["SCC"] == True:
			response = make_response(redirect("/"))
			usernameencrypted = encrypt(username)
			response.set_cookie("username",usernameencrypted)
			passwordencrypted = encrypt(password)
			response.set_cookie("password",passwordencrypted)
			return response
		if check["SCC"] == False:
			return redirect("/login?msg=noscc")
	msg = request.args.get("msg")
	if msg !=None:
		if msg == "scc":
			return render_template("login.html",scc=True)
		else:
			pass
		if msg == "noscc":
			return render_template("login.html",error=True)
	else:
		pass 
	return render_template("login.html")

if __name__ == "__main__":
	app.run(debug=True)
