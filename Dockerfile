# Dockerfile

# Use the official Python image as the base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing .pyc files and to ensure immediate output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies required for your packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pip and pipenv
RUN pip install --upgrade pip && pip install pipenv

# Copy only Pipfile and Pipfile.lock first to leverage Docker caching
COPY Pipfile Pipfile.lock /app/

# Install Python dependencies using pipenv, without creating a virtual environment
RUN pipenv install --deploy --system

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Run migrations and start the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]