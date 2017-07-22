import json , requests

payload = {'url1':'https://scontent.fdel7-1.fna.fbcdn.net/v/t34.0-0/s261x260/20120953_1249496695159626_1508246269_n.jpg?oh=dc5ff4c9ad0fce097b53ef0142f68fed&oe=59744D54' , 'url2':'https://scontent.fdel7-1.fna.fbcdn.net/v/t34.0-0/s261x260/20117462_1249497091826253_1295398522_n.jpg?oh=626316b9f15ea0f97e54c3bd5667b71e&oe=59751A1B'}
payload = json.dumps(payload)

r = requests.post("http://139.59.40.238:8080/about" , data = payload)

print r.text