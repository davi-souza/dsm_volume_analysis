pip install -r requirements.txt

gunicorn --reload --log-level=debug --workers=2 --timeout=1800 --bind=0.0.0.0:$PORT wsgi:app
