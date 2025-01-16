FROM python:3.9-slim
WORKDIR /srv
COPY run.py requirements.txt /srv
COPY templates/index.html /srv/templates/index.html
COPY .env /srv/.env
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "run:app", "-b", ":5000", "-w", "1", "--worker-class", "eventlet", "--timeout", "120"]
