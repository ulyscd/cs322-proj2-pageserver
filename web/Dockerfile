FROM python:3.11-slim
MAINTAINER Ulys Chauncey Drumrongthai "ulys@uoregon.edu"

WORKDIR /app 
COPY . /app

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends build-essential
    
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]