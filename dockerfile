FROM python:3.9.5

WORKDIR /app

COPY requirements.txt . 

RUN pip install -r requirements.txt
RUN pip install nltk
RUN python -m nltk.downloader stopwords

ENV PYTHONPATH="${PYTHONPATH}:/app/frontend"

COPY . /app/
COPY backend/pretreatment ../backend/pretreatment
COPY backend/data/raw_data ../backend/data/raw_data
COPY backend/callbacks ../backend/callbacks
COPY backend/data/model ../backend/data/model
COPY frontend /app/frontend


EXPOSE 4000


CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:4000 frontend.app:server"]
