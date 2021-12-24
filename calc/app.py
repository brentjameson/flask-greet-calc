from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add_nums():
    '''Returns a + b'''
    a = request.args.get('a', type = int)
    b = request.args.get('b', type = int)
    res = str(operations.add(a,b))
    html = f'<html><body><h1>{res}</h1></body></html>'
    return html

@app.route('/sub')
def sub_nums():
    '''Returns a - b'''
    a = request.args.get('a', type = int)
    b = request.args.get('b', type = int)
    res = str(operations.sub(a,b))
    html = f'<html><body><h1>{res}</h1></body></html>'
    return html

@app.route('/mult')
def mult_nums():
    '''Returns a * b'''
    a = request.args.get('a', type = int)
    b = request.args.get('b', type = int)
    res = str(operations.mult(a,b))
    html = f'<html><body><h1>{res}</h1></body></html>'
    return html

@app.route('/div')
def div_nums():
    '''Returns a / b'''
    a = request.args.get('a', type = int)
    b = request.args.get('b', type = int)
    res = str(operations.div(a,b))
    html = f'<html><body><h1>{res}</h1></body></html>'
    return html


