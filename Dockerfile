FROM davisouza/freecad_base:ubuntu.16

WORKDIR /app/mech4u/

COPY . .

RUN pip install -r requirements.txt

CMD bash run.sh
