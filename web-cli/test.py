import requests

page = requests.post("http://localhost:5000/login",data={"username":"efeakaroz13","password":"12345"})



print(page.content)

