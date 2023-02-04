import flask as Flask

app = Flask.Flask("USBot HTTP API")

@app.route("/")
def index():
    return {'code': 200, 'message':'ok', 'version': '0.1.0'}

@app.route("/api/auth/labby1/<password>/<serverIP>", methods=['GET'])
def auth(password, serverip):
    with open('token.txt', 'r') as f:
        pw = f.read()
    pw = str(pw)
    if password != pw:
        return {'code': 403, 'message':'password error'}
    else:
        with open('server.txt', 'w') as f:
            f.write(str(serverip))
        import core