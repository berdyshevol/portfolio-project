# AI Portfolio Site

Django 5 portfolio site built for the Baylor MSIS final project. Showcases eight AI/ML projects, a skills page, a structured resume, and a contact form. Tailwind for styling, dark mode, deployed on Render with Neon Postgres.

**Live:** https://portfolio-8tfs.onrender.com/
(Render free tier — first hit after ~15 min idle takes ~30s to wake)

## Local development

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py tailwind install
python manage.py migrate
python manage.py loaddata initial_projects initial_skills initial_resume
python manage.py createsuperuser
python manage.py runserver
```

In a second terminal:

```bash
python manage.py tailwind start
```

Visit http://127.0.0.1:8000/.

## Tests

```bash
python manage.py test
```

## Deployment

Render web service runs `./build.sh` then `gunicorn portfolio.wsgi`. Required env vars: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`, `DATABASE_URL` (Neon), `DJANGO_SETTINGS_MODULE=portfolio.settings.prod`.
