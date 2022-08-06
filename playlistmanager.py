import os
import random
from tabnanny import check

from flask import redirect
import kauth
import time 
import json 
from cryptography.fernet import Fernet
auth = kauth.kauth("Kentelify")
letterlist = ["I","K","Z","A","T","r","a","M","l"]
key = b'D71kHIq7Wsyrjd30avvyzrS7BTT74lAXBB5y6mllnsQ='
fernet = Fernet(key)


def encrypt(text):
	encodedtext = fernet.encrypt(text.encode())
	return encodedtext.decode()


def decrypt(text):
	encodedtext = fernet.decrypt(text.encode())
	return encodedtext.decode()

class manager:
  def __init__(self,username,password):
    self.username=username
    self.password = password
    outcheck = auth.login(username,password)
    if outcheck["SCC"] == True:
      self.loggedin = True
    else:
      raise ValueError("Username or password is not correct")

  def create_playlist(self,playlistname,description):
    firstletter = random.choice(letterlist)
    secondletter = random.choice(letterlist)
    thirdletter = random.choice(letterlist)
    strout = f"{firstletter}{secondletter}{thirdletter}{random.randint(1,123432955854)}"
    try:
      os.listdir("playlists")
    except:
      os.system("mkdir playlists")
    playlistfile = open(f"playlists/{self.username}.{strout}","w")
    data = json.dumps({"username":self.username,"description":description,"title":playlistname,"time":time.ctime(time.time()),"musics":[]},indent=4)
    encrypteddata = encrypt(str(data))
    playlistfile.write(encrypteddata)

    return {"SCC":True,"id":strout}
  def viewplaylist(self,playlistid):
    authchecker = auth.login(self.username,self.password) 
    if authchecker["SCC"] == True:

      allplaylists = os.listdir("playlists")
      outputlist = []
      for p in allplaylists:
        try:
          playlistfile = p.split(playlistid)[1]

          outputlist.insert(0,p)
        except:
          pass 
      if len(outputlist) == 0:
        return {"SCC":False}
      else:
        myfile = json.loads(decrypt(open("playlists/"+outputlist[0],"r").read()))
        myfile["SCC"]=True
        myfile["id"] = playlistid.replace('.','')
        return myfile
    else:
      raise ValueError("Username or password is not correct")
  
  def playlister(self):
    checkoutput = auth.login(self.username,self.password)
    if checkoutput["SCC"] == True:
      allplaylists = os.listdir("playlists")
      myplaylists = []
      for p in allplaylists:
        try:
          id_ = p.split(self.username)[1]
          myplaylists.append(self.viewplaylist(id_))
        except:
          pass

      
      return myplaylists
    else:
      return redirect("/")
    
  def listallsongs(self):
    output = []
    musiclistfile = open("songs.txt","r")
    for m in musiclistfile.readlines():
      filename = m.split("||--||")[0]
      songname = m.split("||--||")[1]
      data = {
        "filename":filename.replace("\n",""),
        "songname":songname.replace("\n","")
      }
      output.append(data)

    return output