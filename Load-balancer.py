import requests

# Replace this with your load balancer DNS name or IP address
load_balancer_url = 'http://your-load-balancer-dns-name'

# Number of requests to send
num_requests = 10

for i in range(num_requests):
    try:
        response = requests.get(load_balancer_url)
        print(f'Request {i + 1}: Response from {response.text}')
    except requests.RequestException as e:
        print(f'Request {i + 1}: Failed with error {e}')
