import time
import subprocess

while True:
    subprocess.call(["python", "network_probe.py"])
    time.sleep(60)