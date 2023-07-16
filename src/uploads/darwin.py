import socket
import yaml
import subprocess

def execute_pipeline(pipeline):
    results = {}
    for step, command in pipeline.items():
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            results[step] = result.strip()
        except subprocess.CalledProcessError as e:
            results[step] = str(e.output)
    return results

def start_client():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    data = client_socket.recv(4096).decode()

    try:
        pipeline = yaml.safe_load(data)
        results = execute_pipeline(pipeline)
        response = yaml.dump(results)
    except Exception as e:
        response = f"Error al ejecutar la pipeline: {str(e)}"

    client_socket.send(response.encode())
    client_socket.close()

print("Starting Client")
start_client()