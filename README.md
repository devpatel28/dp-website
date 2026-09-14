# Dev Nareshkumar Patel - Portfolio & Resume Web Application

A full-stack, data-driven software developer portfolio and resume website engineered with **Python**, **Django**, and **Docker**.

## 🚀 Key Features

- **Dynamic Data Models**: Skills, projects, work experience, education, and recruiter contact messages are managed via Django's ORM and SQLite/PostgreSQL.
- **Django Admin Interface**: Easily update portfolio projects, skills, and check recruiter messages without touching code (`/admin/`).
- **Modern Responsive UI**: Custom CSS with Dark & Light theme switcher, glassmorphism cards, and mobile navigation.
- **Recruiter PDF / Print View**: Clean print stylesheet (`print.css`) that automatically generates a 1-2 page professional black-and-white executive resume when printing (`Ctrl+P` or clicking "PDF Resume").
- **Containerized Deployment**: Fully Dockerized with multi-stage `Dockerfile` and `docker-compose.yml`.
- **WhiteNoise Static Files**: High-performance static file serving ready for production hosting.

---

## 🛠️ Getting Started (Local Development)

### Quickest Way:
Run the launcher script:
```powershell
python "DP Web.py"
```
Or double-click `run_dev.bat` in Windows File Explorer!

### Manual Setup:
1. **Create and activate a virtual environment**:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```powershell
   python manage.py makemigrations resume
   python manage.py migrate
   ```

4. **Populate initial resume data**:
   ```powershell
   python manage.py seed_data
   ```

5. **Start server**:
   ```powershell
   python manage.py runserver 8000
   ```
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

6. **Create an Admin superuser** (to access `/admin`):
   ```powershell
   python manage.py createsuperuser
   ```

---

## 🐳 Running with Docker

Once Docker Desktop is installed and running on your machine:
```powershell
docker compose up --build
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🔗 Linking GitHub to VS Code & Pushing this Project

You already have a GitHub account: [https://github.com/devpatel28](https://github.com/devpatel28)

### Step 1: Sign In to GitHub in VS Code
1. In the bottom-left corner of VS Code, click the **Accounts** icon (silhouette of a person or gear).
2. Click **"Sign in with GitHub"**.
3. A browser window will open asking to authorize Visual Studio Code. Click **Authorize**.
4. Return to VS Code; you will see your GitHub profile icon in the Accounts menu.

### Step 2: Initialize Git and Commit Your Project
In your VS Code terminal (PowerShell), run:
```powershell
git init
git config user.name "devpatel28"
git config user.email "dnhp281999@gmail.com"
git add .
git commit -m "Initial commit: Dev Patel Django resume website and Docker setup"
```

### Step 3: Publish to GitHub via VS Code
1. On the left activity bar of VS Code, click the **Source Control** tab (`Ctrl + Shift + G`).
2. Click the blue **"Publish Branch"** or **"Publish to GitHub"** button.
3. Choose either **"Publish to GitHub public repository"** (recommended for recruiters to view your code) or **private**.
4. VS Code will automatically create `https://github.com/devpatel28/dp-website` and push all your code!
