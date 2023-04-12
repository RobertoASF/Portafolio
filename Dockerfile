FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /Container-tindplace
COPY requirements.txt /Container-tindplace/
RUN pip install -r requirements.txt
COPY . /Container-tindplace/