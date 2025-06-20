FROM python:3.10-slim

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app
COPY . .

# Cloud Run expects app to listen on $PORT
ENV PORT=8080

CMD ["python", "app.py"]