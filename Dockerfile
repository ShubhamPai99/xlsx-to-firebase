FROM registry.cigna.com/redhat/python-39-rhel8:latest

WORKDIR /app
COPY . .

RUN pip install pandas && pip install openpyxl && pip install firebase_admin
RUN python3 upload.py
