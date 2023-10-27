FROM 

WORKDIR /app
COPY . .

RUN pip install pandas && pip install openpyxl && pip install firebase_admin
RUN python3 upload.py
