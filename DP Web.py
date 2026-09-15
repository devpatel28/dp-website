"""
DP Web.py - Dev Patel's Portfolio & Resume Website Launcher
Runs the Django development server and opens the website in your browser.
"""

import os
import sys
import subprocess
import webbrowser
import time
import threading


def run_command(command):
    print(f"--> Running: {' '.join(command)}")
    result = subprocess.run(command, check=True)
    return result


import socket


def find_available_port(start_port=8080, max_port=8999):
    """Finds an available TCP port starting from start_port."""
    for port in range(start_port, max_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            # If connect_ex returns non-zero, the port is free
            if sock.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return start_port


def open_browser(port):
    time.sleep(1.5)
    url = f"http://127.0.0.1:{port}"
    print(f"--> Opening browser to {url}...")
    webbrowser.open(url)


def main():
    print("=" * 60)
    print("Dev Nareshkumar Patel - Resume & Portfolio Web Platform")
    print("=" * 60)

    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    # Check dependencies
    try:
        import django
        print(f"[OK] Django version {django.get_version()} detected.")
    except ImportError:
        print("[!] Django not detected. Installing dependencies from requirements.txt...")
        run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    # Run migrations
    print("[*] Running database migrations...")
    subprocess.run([sys.executable, "manage.py", "makemigrations", "resume"])
    subprocess.run([sys.executable, "manage.py", "migrate"])

    # Seed data
    print("[*] Ensuring resume data is populated...")
    subprocess.run([sys.executable, "manage.py", "seed_data"])

    # Automatically find an available port to avoid conflicts
    port = find_available_port(8080)
    print(f"[+] Using local port: {port}")

    # Launch browser thread
    threading.Thread(target=open_browser, args=(port,), daemon=True).start()

    # Start Django server on detected free port
    print(f"\n[+] Starting Django development server at http://127.0.0.1:{port}")
    print("[+] Press CTRL+C in this terminal to stop the server.\n")
    try:
        subprocess.run([sys.executable, "manage.py", "runserver", str(port)])
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")


if __name__ == '__main__':
    main()

