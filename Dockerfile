FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /var/www/html/project

COPY ./req.txt .

RUN apt-get update && apt-get install -y \
build-essential \
libpq-dev \
libjpeg-dev \
zlib1g-dev \
libhdf5-dev \
gcc \
pkg-config \
python3-dev \
&& rm -rf /var/lib/apt/lists/* 



RUN pip3 install --upgrade pip && pip3 install --timeout=60 --retries=5 -r req.txt

COPY . /var/www/html/project

# RUN python /var/www/html/project/manage.py migrate


# EXPOSE 8000

# CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000" ]