# Use the official Python image as base
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the STATIC_ROOT directory exists
RUN mkdir -p /app/staticfiles

# Expose the port Gunicorn will run on
EXPOSE 8000

# Run migrations and collect static files
RUN python manage.py migrate && python manage.py collectstatic --noinput

# Create superuser if not exists
RUN python manage.py createsuperuser --noinput || true

# Start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "api.wsgi:application"]
