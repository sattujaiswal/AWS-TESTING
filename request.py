import requests

# URL of your FastAPI endpoint
url = "http://ec2-54-167-32-133.compute-1.amazonaws.com:8000/"

# Send GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content (the numbers from 1 to 10)
    print(response.text)
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
