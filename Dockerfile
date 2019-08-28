FROM davisouza/freecad_base:ubuntu.16

WORKDIR /app/mech4u/

COPY . .

RUN pip install -r requirements.txt

ENV PORT=443

CMD gunicorn --workers=2 --timeout=1800 --bind=0.0.0.0:$PORT wsgi:app
