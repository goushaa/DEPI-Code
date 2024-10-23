# DNS Resolver Script 

This Python script continuously resolves the internal DNS name of an Nginx service deployed in Kubernetes and prints the resolved IP address. The script runs in a loop, attempting to resolve the DNS at a configurable interval.

## Features

- Resolves the DNS of the Nginx service inside a Kubernetes cluster.
- Configurable resolution interval via an environment variable.
- Prints the resolved IP address or an error message if the resolution fails.

## Requirements

- Python3
```bash
sudo apt install python3
```

## Configuration

You can configure the interval at which the DNS is resolved using the environment variable `DNS_RESOLVE_INTERVAL_SECONDS`. If this variable is not set, it defaults to 10 seconds.

### Setting the Environment Variable

In your terminal, set the environment variable as follows:

```bash
export DNS_RESOLVE_INTERVAL_SECONDS="5"
```
Replace `5` with your desired interval (in seconds) for DNS resolution.

### Docker Setup

If you plan to run this script in a Docker container, you can pass the environment variable like this:

```bash
docker run -e DNS_RESOLVE_INTERVAL_SECONDS="5" goushaa/internal-dns-resolver
```

## Applying the Deployment

To deploy the DNS resolver, save the above YAML to a file named `dns-resolver-deployment.yaml`, and then apply it to your Kubernetes cluster:

```bash
kubectl apply -f dns-resolver-deployment.yaml
```

After deploying, you can check the logs of the DNS resolver pod to see the resolved IP addresses: 

```bash
kubectl logs -l app=dns-resolver
```
