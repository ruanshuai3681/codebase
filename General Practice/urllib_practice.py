import urllib_practice

# Create a connection pool with urllib3
http = urllib3.PoolManager()

# Specify the URL you want to make a request to
url = 'https://www.abc.com'

# Make a GET request
response = http.request('GET', url)

# Print the status code and content of the response
print(f"Status Code: {response.status}")
print("Response Content:")
print(response.data.decode('utf-8'))
