from os import abort
from tabnanny import check
from unicodedata import name
from flask import Flask, render_template, request, redirect, make_response, abort
from flask_cors import CORS
from kauth import kauth
from cryptography.fernet import Fernet
from playlistmanager import manager

key = b'D71kHIq7Wsyrjd30avvyzrS7BTT74lAXBB5y6mllnsQ='
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
    if username == None or username.strip() == "":

        return render_template("base.html")
    else:
        username = decrypt(username)
        password = decrypt(request.cookies.get("password"))

        outcheck = auth.login(username, password)
        if outcheck["SCC"] == True:
            try:
                myapp = manager(username, password)
                myplaylists = myapp.playlister()
                return render_template("home.html",playlists=myplaylists)

            except Exception as e:
                return str(e)

        else:
            return render_template("base.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    msg = request.args.get("msg")
    if msg != None:
        if msg == "noscc":
            return render_template("register.html", error=True)

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        fullname = request.form.get("fullname")
        response = auth.createuser(
            username=username, password=password, fullname=fullname)
        if response["SCC"] == True:
            return redirect("/login?msg=scc")
        if response["SCC"] == False:
            return redirect("/register?msg=noscc")
    return render_template("register.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        check = auth.login(username, password)
        if check["SCC"] == True:
            response = make_response(redirect("/"))
            usernameencrypted = encrypt(username)
            response.set_cookie("username", usernameencrypted)
            passwordencrypted = encrypt(password)
            response.set_cookie("password", passwordencrypted)
            return response
        if check["SCC"] == False:
            return redirect("/login?msg=noscc")
    msg = request.args.get("msg")
    if msg != None:
        if msg == "scc":
            return render_template("login.html", scc=True)
        else:
            pass
        if msg == "noscc":
            return render_template("login.html", error=True)
    else:
        pass
    return render_template("login.html")


@app.route("/create_playlist", methods=["POST", "GET"])
def createplaylist():
    username = request.cookies.get("username")
    password = request.cookies.get("password")
    try:
        username = decrypt(username)
        password = decrypt(password)
        mymanager = manager(username, password)

        if request.method == "POST":
            playlistname = request.form.get("playlistname")
            description = request.form.get("description")
            mymanager.create_playlist(playlistname, description)
            return redirect("/")
        if request.method == "GET":
            return render_template("create.html")

    except:
        return redirect("/")


@app.route("/playlist/<playlist_id>")
def playlist(playlist_id):

    username = request.cookies.get("username")
    if username == None:
        return abort(403)
    else:
        username = decrypt(username)
        password = decrypt(request.cookies.get("password"))
        try:
            mymanager = manager(username, password)
            checkout = mymanager.viewplaylist(playlistid=playlist_id)
            if checkout["SCC"] == True:
                return checkout
            else:
                return"404"
        except Exception as e:
            return str(e)


@app.route("/admin",methods=["POST","GET"])
def admin():

	username = request.cookies.get("username_")
	password = request.cookies.get("password_")
	
	if username == None:
		if request.method == "POST":
			username = request.form.get("username")
			password = request.form.get("password")
			if username == "admin" and password =="12345":
				response = make_response(redirect("/admin"))
				response.set_cookie("username_",encrypt(username))
				response.set_cookie("password_",encrypt(password))
				return response
			else:
				return render_template("adminlogin.html",err=True)
		return render_template("adminlogin.html")
	else:
		try:
			username = decrypt(username)
			password = decrypt(password)
			if username == "admin" and password =="12345":
				return render_template("admin.html") 
		except:
			return render_template("adminlogin.html")
if __name__ == "__main__":
    app.run(debug=True)
