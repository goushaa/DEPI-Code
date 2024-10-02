# Nginx Health Check Script

This Python script periodically checks the health of an Nginx service by sending HTTP requests to a specified IP address and port. It prints the response status code and a snippet of the response body.

## Features

- Checks the Nginx service health every 5 seconds.
- Configurable IP address via an environment variable.
- Prints the HTTP response status and a preview of the response body.

## Requirements

- Python3
```bash
sudo apt install python3
```

## Configuration

Before running the script, you can set the environment variable `NGINX_SERVICE_IP` to specify the IP address of your Nginx service. If this variable is not set, it will default to `8.8.8.8`.

### Setting the Environment Variable

In your terminal, you can set the environment variable as follows:

```bash
export NGINX_SERVICE_IP="your_new_ip_address"
```
Replace `your_new_ip_address` with the actual IP address of your Nginx service.

## Usage

To run the script, use Python:

```bash
python3 nginx_health_check.py
```

