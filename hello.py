from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def dump_headers(path):
    print(request.headers)

    return render_template('hello.html')
