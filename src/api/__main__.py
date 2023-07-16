from flask import Flask, request, redirect
from logger import Logger
from env import App
from time import strftime
import traceback
import os

ctx = Logger(name=App.name, log_level=App.log_level)
app = Flask(__name__)

# disable logging flask
import logging
app.logger.disabled = True
log = logging.getLogger('werkzeug')
log.disabled = True
import flask.cli    
flask.cli.show_server_banner = lambda *args: None

def runner():
    ctx.printable(function=__package__, message=f"Listen: {App.api_host}:{App.api_port}")
    app.run(host=App.api_host, port=App.api_port)

@app.after_request
def after_request(response):
    ctx.printable(__package__, f"{strftime('[%Y-%b-%d %H:%M]')} {request.remote_addr} {request.method} {request.scheme} {request.full_path} {response.status}")
    return response

@app.errorhandler(Exception)
def exceptions(e):
    ctx.error(__package__, f"{strftime('[%Y-%b-%d %H:%M]')} {request.remote_addr} {request.method} {request.scheme} {request.full_path} 5xx INTERNAL SERVER ERROR\n{traceback.format_exc()}")
    return e.status_code

@app.route('/', methods=['GET'])
def welcome():
    client_type = request.headers['User-Agent']

    if client_type == 'Darwin':
        return get_file('darwin.py')
    else:
        return "Hello World!\n"

def root_dir(): 
    return os.path.abspath(os.path.dirname(__file__))

def get_file(filename):
    try:
        src = os.path.join(f"{App.root_dir}/uploads", filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)