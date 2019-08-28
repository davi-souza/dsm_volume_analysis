pip install -r requirements.txt

gunicorn --workers=2 --timeout=1800 --bind=0.0.0.0 wsgi:app
