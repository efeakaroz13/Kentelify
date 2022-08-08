from os import abort
from tabnanny import check
from unicodedata import name
from flask import Flask, render_template, request, redirect, make_response, abort
from flask_cors import CORS
from kauth import kauth
from cryptography.fernet import Fernet
from playlistmanager import manager
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
import json
import urllib.request
import re
import time
from pytube import YouTube
import os
from colorama import Fore, Back, Style

def compress(basename):
		os.system(f"ffmpeg -y -i '{basename}.mp4' -vcodec libx265 -crf 28 '{basename}_C.mp4'")

class Downloader:
	def downloadvideo(search):
		search = search.lower().replace("ü","u").replace("$","s").replace("ö","").replace("ş","s").replace("ö","o").replace("İ","I").replace("ı","i")
		try:
			page = urllib.request.urlopen("https://www.youtube.com/results?search_query={}".format(search.replace(' ','+')))
			videoids=  re.findall(r"watch\?v=(\S{11})",page.read().decode())
			theurl = "https://youtube.com/watch?v="+videoids[0]

			yt = YouTube(theurl)
			print(Fore.BLUE,"DOWNLOADING | {}".format(yt.title))
			
			video = yt.streams.filter(only_audio=True).first()
			
			
			out_file = video.download(output_path="./static")
			base, ext = os.path.splitext(out_file)
			compress(base)
			os.system(f"ffmpeg -y -i '{base}_C.mp4' -b:a 192K -vn '{base}.mp3'")
			os.system(f"rm '{base}.mp4'") 
			os.system(f"rm '{base}_C.mp4'")

			print(Fore.GREEN,"COMPLETE | {}".format(yt.title))
			print(Style.RESET_ALL,"\n")
			return f"/static/{base.split('/')[-1]}.mp3"
		except:
			print(Fore.RED,"NETWORK ERR - Retrying in 10 seconds")
			print(Style.RESET_ALL)
			time.sleep(10)
			page = urllib.request.urlopen("https://www.youtube.com/results?search_query={}".format(search.replace(' ','+')))
			videoids=  re.findall(r"watch\?v=(\S{11})",page.read().decode())
			theurl = "https://youtube.com/watch?v="+videoids[0]
			
			yt = YouTube(theurl)
			print(Fore.BLUE,"DOWNLOADING | {}".format(yt.title))
			
			video = yt.streams.filter(only_audio=True).first()
			
			
			out_file = video.download(output_path="./static")
			base, ext = os.path.splitext(out_file)

			compress(base)
			os.system(f"ffmpeg -y -i '{base}_C.mp4' -b:a 192K -vn '{base}.mp3'")
			os.system(f"rm '{base}.mp4'") 
			os.system(f"rm '{base}_C.mp4'")

			print(Fore.GREEN,"COMPLETE | {}".format(yt.title))
			print(Style.RESET_ALL,"\n")
			return f"/static/{base.split('/')[-1]}.mp3"





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


@app.route("/playlister_api/<playlist_id>")
def playlisterapi(playlist_id):
	client_id = "a0c932b9e34b4149b8f367c5e403313e"
	secretclient = "37335ef57fad4854825c67826b6a5816"
	os.environ["SPOTIPY_CLIENT_ID"] =client_id
	os.environ["SPOTIPY_CLIENT_SECRET"] =secretclient



	sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

	offset = 0

	response = sp.playlist_items(playlist_id,
								offset=offset,
								fields='items.track,total')

	output = {"out":[],"lengtha":0}
	for r in response['items']:
		outp = str(r['track']['name'])+" "+str(r['track']['artists'][0]['name'])
		output["out"].append(outp)
	output["lengtha"] = len(output["out"])
	return output

@app.route("/download/by_search")
def download_by_search():
	q = request.args.get("q")
	try:
		username = decrypt(request.cookies.get("username_"))
		password = decrypt(request.cookies.get("password_"))
		if username == "admin" and password =="12345":
			try:
				out = Downloader.downloadvideo(q)
				namewriter = open("songs.txt","a")
				namewriter.write(str(out)+"||--||"+q+"\n")
				return {"SCC":True,"filename":out}
			except:
				return {"SCC":False,"filename":""}
	except:
		return abort(403)


@app.route("/play")
def player():
	songname = request.args.get("songname")
	songlister = open("songs.txt","r").readlines()
	for r in songlister:
		try:
			r.split("||--||")[1].lower().split(songname.lower())[1]
			return render_template("play.html",file_=r.split("||--||")[0],name=r.split("||--||")[1])
		except:
			pass

	return "404"
@app.route("/remove/playlist/<playlist_id>")
def removeplaylist(playlist_id):
	try:
		username = decrypt(request.cookies.get("username"))
		password = decrypt(request.cookies.get("password"))
		mymanager = manager(username,password)
		output = mymanager.viewplaylist(playlist_id)
		if output["username"] == username:
			os.system(f"rm 'playlists/{username}.{playlist_id}'")
			return redirect("/")
		else:
			return redirect("/")

	except:
		return redirect("/")
@app.route("/playlistview/<playlistid>")
def playlistviewandedit(playlistid):
	try:
		username = decrypt(request.cookies.get("username"))
		password = decrypt(request.cookies.get("password"))
		playlistmanager= manager(username,password)
		myplaylist = playlistmanager.viewplaylist(playlistid)
		return render_template("playlisr10.html",playlistdata=myplaylist)
	except Exception as e:
		print(e)
		return redirect("/")


@app.route("/add_song/<playlist_id>")
def add_song(playlist_id):
	musicfile = request.args.get("file")
	musicname = request.args.get("music")
	if musicname == None or musicfile == None:
		return {"SCC":False,"err":"Music name or file is not specified."}
	try:
		username = decrypt(request.cookies.get("username"))
		password = decrypt(request.cookies.get("password"))

		mymanager= manager(username,password)
		myplaylist = mymanager.viewplaylist(playlistid=playlist_id)
		if myplaylist["username"] == username.strip():
			playlist_reader = json.loads(decrypt(open(f"playlists/{username}.{myplaylist['id']}","r").read()))
			data = {"file":musicfile,"musicname":musicname}
			try:
				playlist_reader["musics"].index(data)
				print("INFO | PASSING")
			except:
				playlist_reader["musics"].insert(0,data)
				writervariable = open(f"playlists/{username}.{myplaylist['id']}","w")
				writervariable.write(encrypt(json.dumps(playlist_reader,indent=4)))
		return redirect("/playlistview/{}".format(playlist_id))
	except Exception as e:
		print(e)
		return redirect("/")

@app.route("/songlister")
def songlister():
	try:
		username = decrypt(request.cookies.get("username"))
		password = decrypt(request.cookies.get("password"))
		mymanager = manager(username,password)
		allsongs = mymanager.listallsongs()
		return {"SCC":True,"out":allsongs,"counter":len(allsongs)}
	except:
		return {"SCC":False,"err":"Login credentials"}


@app.route("/remove_song/<playlistid>")
def song_Remove(playlistid):
	try:
		username = decrypt(request.cookies.get("username"))
		password = decrypt(request.cookies.get("password"))
	except:
		return abort(403)

	mymanager=manager(username,password)
	songname = request.args.get("music")
	try:
		myplaylist = json.loads(decrypt(open(f"playlists/{username}.{playlistid}","r").read()))
	except:
		return redirect("/")
	playlistfile = open(f"playlists/{username}.{playlistid}","w")
	musics = myplaylist["musics"]
	for m in musics:
		if m["musicname"] == songname:
			musics.pop(musics.index(m))
		else:
			pass
	data = json.dumps(myplaylist, indent=4)
	encrypteddata = encrypt(str(data))
	playlistfile.write(encrypteddata)
	return redirect("/playlistview/{}".format(playlistid))

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0")
