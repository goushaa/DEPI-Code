import socket
import time
import requests

# Public IP and port of the Nginx service
nginx_service_ip = "18.212.116.251"
nginx_service_port = 30515

def check_nginx():
    try:
        response = requests.get(f"http://{nginx_service_ip}:{nginx_service_port}/")
        print(f"Response from Nginx: {response.status_code} - {response.text[:100]}")  # Print the first 100 chars of response
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to Nginx: {e}")

while True:
    check_nginx()
    time.sleep(5)  # Check every 5 seconds
