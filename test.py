import requests

url = "http://127.0.0.1:5000/classify"
payload = {
    "email": "Hi, my name is Alice Smith. My email is alice.smith@example.com and my phone number is +91 9876543210. My aadhar is 1234-5678-9012. I'm facing an issue with my payment."
}

response = requests.post(url, json=payload)

print(response.json())
