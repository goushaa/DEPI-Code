import os
import socket
import time
import requests

# Get the public IP and port of the Nginx service from environment variables
nginx_service_ip = os.getenv("NGINX_SERVICE_IP", "8.8.8.8")  # Default value if env variable is not set
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
