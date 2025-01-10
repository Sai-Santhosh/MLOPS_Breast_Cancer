import os
import subprocess

# Uninstall all packages in requirements.txt
with open("requirements.txt", "r") as file:
    packages = file.read().splitlines()

if packages:
    subprocess.run(["pip", "uninstall", "-y"] + packages)

# Reinstall all packages in requirements.txt
subprocess.run(["pip", "install", "-r", "requirements.txt"])

print("Uninstallation and reinstallation completed.")