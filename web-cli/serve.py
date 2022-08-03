from flask import Flask ,request,redirect,render_template,make_response,abort
from flask_cors import CORS 
import kauth


app = Flask(__name__)
CORS(app)
auth = kauth.kauth("Kentelify")

@app.errorhandler(403)
def forothree(e):
	return {"ERR":"403 FORBIDDEN"}


@app.route("/login",methods=["POST","GET"])
def login_forapp():
	print(request.method)
	if request.method == "POST":
		print("DUMBASS")
		username = request.form.get("username")
		password = request.form.get("password")
		print(username)
		print(password)
		checkout = auth.login(username,password)
		if checkout["SCC"] == False:
			return abort(403)
		else:
			return {"SCC":True}

	if request.method == "GET":
		return abort(403)


app.run(debug=True)