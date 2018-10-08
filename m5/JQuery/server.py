import json

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route("/")
def index():
    resp = Response("<h2>首页</h2>")
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route("/course")
def course():
    resp = Response(json.dumps({
        "name": "张三",
    }))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route("/create", methods = ["post",])
def create():
    print(request.form.get('name'))

    with open('user.json','r') as f:
        data = json.loads(f.read())
    
    data.append({"name": request.form.get('name')})

    with open('user.json','w') as f:
        f.write(json.dumps(data))

    resp = Response(json.dumps(data))
    
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

if __name__ == '__main__':
    app.run(host = "localhost",port = 8880,)    
