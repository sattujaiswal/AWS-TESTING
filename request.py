import requests

# Correct URL with the port number separated from the path
url = "http://ec2-18-208-230-177.compute-1.amazonaws.com:8000/fibonacci/10000"

# Send GET request
response = requests.get(url)

# Print the response text
print(response.text)

# print("-----------------------")
# response = requests.get("http://ec2-184-73-42-14.compute-1.amazonaws.com:8000/")
# print(response.text)

# import requests

# # Replace 'your-load-balancer-dns-name-or-ip-address' with your actual load balancer's DNS name or IP address
# load_balancer_url = 'http://load-balancer-742144782.us-east-1.elb.amazonaws.com'

# try:
#     # Send an HTTP GET request to the load balancer's URL
#     response = requests.get(load_balancer_url)
    
#     # Check if the response was successful (status code 200)
#     if response.status_code == 200:
#         print("Request successful")
#         print("Response content:")
#         print(response.text)
#     else:
#         print(f"Request failed with status code {response.status_code}")
# except requests.RequestException as e:
#     # Handle any exceptions that occur during the request
#     print("An error occurred:", e)

