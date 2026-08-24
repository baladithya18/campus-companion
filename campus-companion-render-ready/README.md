# Campus Companion

A full-stack Django dashboard for students to organize courses, timetable classes, assignment deadlines, notes, and campus events.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Then open http://127.0.0.1:8000.

## Publish online with Render

1. Create a new GitHub repository and upload all project files (including `render.yaml`).
2. Sign in to Render with GitHub, choose **New +** → **Blueprint**, and select that repository.
3. Render reads `render.yaml`, creates the web service and PostgreSQL database, and deploys the app.
4. Once deployment completes, copy the public `.onrender.com` URL from the Render dashboard and share it.
