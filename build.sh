#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py tailwind install --no-input
python manage.py tailwind build --no-input

python manage.py collectstatic --no-input
python manage.py migrate --no-input

if [[ -n "${SEED_FIXTURES:-}" ]]; then
  python manage.py loaddata initial_projects initial_skills initial_resume
fi
