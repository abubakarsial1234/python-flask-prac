# Base image Python ka istemal karein
FROM python:3.9-slim

# Kaam karne ke liye aik directory set karein
WORKDIR /app

# Requirements file copy karein aur install karein
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Baqi code copy karein
COPY . .

# Container ko batayein ke port 5000 par listen karna hai
EXPOSE 5000

# Container start hone par yeh command chalayein
CMD ["python", "app.py"]