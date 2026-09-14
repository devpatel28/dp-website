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


def open_browser():
    time.sleep(1.5)
    print("--> Opening browser to http://127.0.0.1:8000...")
    webbrowser.open("http://127.0.0.1:8000")


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

    # Launch browser thread
    threading.Thread(target=open_browser, daemon=True).start()

    # Start Django server
    print("\n[+] Starting Django development server at http://127.0.0.1:8000")
    print("[+] Press CTRL+C in this terminal to stop the server.\n")
    try:
        subprocess.run([sys.executable, "manage.py", "runserver", "8000"])
    except KeyboardInterrupt:
        print("\n[*] Server stopped.")


if __name__ == '__main__':
    main()
