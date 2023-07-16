from os import environ, path, getcwd

class App():

    # common
    name = environ.get('APP_NAME', 'c2-toy')
    log_level = environ.get('APP_LOG_LEVEL', 'DEBUG')
    root_dir = f"{getcwd()}"

    # server
    server_host = environ.get('SERVER_HOST', '0.0.0.0') 
    server_port = int(environ.get('SERVER_PORT', '12345'))

    # api
    api_host = environ.get('API_HOST', '0.0.0.0')
    api_port = int(environ.get('API_PORT', '9090'))