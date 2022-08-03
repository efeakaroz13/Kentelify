'''
K7 KENTEL AUTH MODULE BY EFE AKARÖZ
2022
JULY
22TH

WITH PYTHON AND C
EDITOR:VSCODE
'''
import subprocess
import os


class kauth:
    def __init__(self, project_name):
        self.projname = project_name

    def createuser(self, username, password, fullname=None, city=None, birthyear=None, talents=None):
        if username == None:
            return {"SCC": False, "err": "USERNAME CAN'T BE NONE!", "project": self.projname}
        if password == None:
            return {"SCC": False, "err": "YOU NEED TO SPECIFY PASSWORD!", "project": self.projname}

        try:
            os.listdir("users")
        except:
            os.system("mkdir users")
        try:
            open(f"users/{username}.K7USERFILE", "r")

            return {"SCC": False, "err": "USER EXISTS", "project": self.projname}
        except:
            checkout = str(subprocess.check_output(
                f"./auth-module login {username} {password}", shell=True))
            try:
                checkout.split("200")[1]
                return {"SCC": False, "err": "USER EXISTS", "project": self.projname}

            except:

                userfile = open(f"users/{username}.K7USERFILE", "a")
                if fullname == None:
                    fullname = "EMPTY"
                if city == None:
                    city = "EMPTY"
                if birthyear == None:
                    birthyear = "EMPTY"
                if talents == None:
                    talents = "EMPTY"

                userfile.write("PROJECT={};--;\n".format(self.projname))
                userfile.write("USERNAME={};--;\n".format(username))
                userfile.write("PASSWORD={};--;\n".format(password))
                userfile.write("FULLNAME={};--;\n".format(fullname))
                userfile.write("CITY={};--;\n".format(city))
                userfile.write("BIRTHYEAR={};--;\n".format(birthyear))
                userfile.write("TALENTS={}".format(talents))
                userfile.write(";--;")

                userfile.close()
                theout = str(subprocess.check_output(
                    f"./auth-module register {username} {password}", shell=True))
                try:
                    theout.split("200")[1]
                    return {"SCC": True, "err": "", "project": self.projname}
                except:
                    return {"SCC": False, "err": "C MODULE FAILED!", "project": self.projname}

    def login(self, username, password):
        try:
            out = str(subprocess.check_output(
                f"./auth-module login {username} {password}", shell=True))
        except Exception as e:

            return {"SCC": False, "err": "MODULE ERR", "porject": self.projname}
        try:
            out.split("200")[1]
            return {"SCC": True, "err": "", "project": self.projname}

        except Exception as e:

            try:
                out.split("403p")[1]
                return {"SCC": False, "err": "WRONG PASSWORD", "project": self.projname}
            except:
                return {"SCC": False, "err": "USER NOT EXISTS", "project": self.projname}

    def getuser(self, username):
        try:
            profilefile = open(f"users/{username}.K7USERFILE", "r").read()
        except:
            return {"SCC": False, "err": "USER DOES NOT EXIST", "platform": self.projname}

        information = profilefile.split(";--;")

        talents = str(profilefile.split("TALENTS=")[1]).replace(";--;", "")
        for i in information:
            try:
                i.split("TALENTS=")[1]
                break
            except:
                try:
                    projectname = i.split("PROJECT=")[1]
                except:
                    try:
                        username = i.split("USERNAME=")[1]
                    except:
                        try:
                            password = i.split("PASSWORD=")[1]
                        except:
                            try:
                                fullname = i.split("FULLNAME=")[1]
                            except:
                                try:
                                    city = i.split("CITY=")[1]
                                except:
                                    try:
                                        birthyear = i.split("BIRTHYEAR=")[1]

                                    except:
                                        pass
        return {"projectname": projectname, "username": username, "password": password, "fullname": fullname, "city": city, "birthyear": birthyear, "talents": talents}

    def changepassword(self, username, password, newpassword):
        outcheck = str(subprocess.check_output(
            f"./auth-module login {username} {password}", shell=True))
        try:
            outcheck.split("200")[1]

            authfileopen = open("auth.txt", "r")
            data = authfileopen.readlines()
            for a in data:

                if str(a.split("🇹🇷")[0]) == username:
                    print("a")
                    if str(a.split("🇹🇷")[1].replace("\n", "")) == password:
                        print("b")
                        data[data.index(a)] = f"{username}🇹🇷{newpassword}\n"
                        break
                    else:
                        pass
                else:
                    pass

            with open('auth.txt', 'w') as outauth:
                outauth.writelines(data)
            userfilepasswordchange = open(f"users/{username}.K7USERFILE", "r")
            userfilepasswordchangedata = userfilepasswordchange.readlines()
            userfilepasswordchangedata[2] = f"PASSWORD={newpassword};--;\n"
            with open(f"users/{username}.K7USERFILE", 'w') as outauth2:
                outauth2.writelines(userfilepasswordchangedata)

            return {"SCC": True, "err": "", "project": self.projname}

        except Exception as e:
            print(e)
            return {"SCC": False, "err": "PASSWORD OR USERNAME IS NOT CORRECT", "project": self.projname}

    def removeuser(self, username, password):
        checkout = str(subprocess.check_output(
            f"./auth-module login {username} {password}", shell=True))
        try:
            checkout.split("200")[1]
            os.system(f"rm users/{username}.K7USERFILE")
            allusers = open("auth.txt", "r")
            allusersdata = allusers.readlines()
            for a in allusersdata:
                if a.split("🇹🇷")[1] == password and a.split("🇹🇷")[0] == username:
                    allusersdata[allusersdata.index(a)] = ""
                    break

            with open('auth.txt', 'w') as thedata:
                thedata.writelines(allusersdata)

            return {"SCC": True, "err": "", "project": self.projname}
        except Exception as e:
            # print(e)
            return {"SCC": False, "err": "INVALID EMAIL OR PASSWORD", "project": self.projname}

