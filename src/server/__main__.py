import socket
import yaml
from logger import Logger
from env import App
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ctx = Logger(name=App.name, log_level=App.log_level)

def runner():
    server_socket.bind((App.server_host, App.server_port))
    server_socket.listen(1)
    ctx.printable(function=__package__, message=f"Listen: {App.server_host}:{App.server_port}")
    ctx.printable(function=__package__, message=f"Server Ready to Receive Connections")
    while True:
        try:
            connection, address = server_socket.accept()
            ctx.printable(function=__package__, message=f"Client Connected {address[0]}:{address[1]}", debug=False)
            with open(f"{App.root_dir}/utils/pipeline.yaml") as f:
                data = yaml.safe_load(f)

            connection.send(json.dumps(data).encode('utf-8'))
            response = connection.recv(4096).decode()

            print(f"[{address[0]}:{address[1]}]:\n{yaml.dump(yaml.safe_load(response),indent=2)}")

            connection.close()
        except Exception as err:
            ctx.error(__package__, err)
            server_socket.close()