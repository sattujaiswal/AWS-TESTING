import requests

# Correct URL with the port number separated from the path
url = "http://ec2-44-211-207-10.compute-1.amazonaws.com:8000/fibonacci/10"

# Send GET request
response = requests.get(url)

# Print the response text
print(response.text)
