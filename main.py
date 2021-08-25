from flask import Flask, request

app = Flask(__name__)


@app.route('/reflect')
def reflect_page():
    return {"headers": dict(request.headers),
            "args": dict(request.args),
            "url": str(request.url)}
