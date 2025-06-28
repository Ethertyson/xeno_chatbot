# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies (optimized for Docker caching)
COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the app
CMD ["gunicorn", "--workers=1", "--threads=1", "--timeout=180", "--preload", "--bind", "0.0.0.0:5000", "run:app"]

# Label for the service
LABEL railway.service="web"