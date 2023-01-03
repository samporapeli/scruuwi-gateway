import os

# username is the id of the gateway device
username = "Raspberry Pi 1"
password = "your_password_here"
logging = True
if os.getenv("DEBUG"):
    api_endpoint = "http://localhost:3000"
else:
    # make sure to use https
    api_endpoint = "https://your_endpoint_here"
