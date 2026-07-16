import socket
import platform
import requests


print("=" * 50)
print("        NETWORK INFORMATION")
print("=" * 50)

# Host Name
hostname = socket.gethostname()
print("Host Name        :", hostname)

# Local IP
local_ip = socket.gethostbyname(hostname)
print("Local IP Address :", local_ip)

# Public IP
try:
    public_ip = requests.get("https://api.ipify.org").text
    print("Public IP        :", public_ip)
except:
    print("Public IP        : No Internet")

# Operating System
print("Operating System :", platform.system())

# OS Version
print("OS Version       :", platform.release())

# Python Version
print("Python Version   :", platform.python_version())

print("=" * 50)