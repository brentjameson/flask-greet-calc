from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome_user():
    '''Return welcome message'''
    html = '<html><body><h1>welcome</h1></body></html>'
    return html

@app.route('/welcome/home')
def welcome_user_home():
    '''Return welcome message'''
    html = '<html><body><h1>welcome home</h1></body></html>'
    return html

@app.route('/welcome/back')
def welcome_user_back():
    '''Return welcome message'''
    html = '<html><body><h1>welcome back</h1></body></html>'
    return html