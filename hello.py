from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/saml2/request')
def saml_request():
    print(request.headers)
    return render_template('hello.html', title='SAML2/request')

@app.route('/saml2/response')
def saml_response():
    print(request.headers)
    return render_template('hello.html', title='SAML2/response')
    
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    print(request.headers)
    return render_template('hello.html', title='Request Info')
