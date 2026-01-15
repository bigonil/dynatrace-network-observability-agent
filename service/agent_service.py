import time
import subprocess
import sys
import os

BASE_DIR = os.path.dirname(sys.executable)

EXTENSION_SCRIPT = os.path.join(
    BASE_DIR,
    "network_probe.py"
)

INTERVAL = 60

def main():
    while True:
        try:
            subprocess.call([sys.executable, EXTENSION_SCRIPT])
        except Exception:
            pass
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()