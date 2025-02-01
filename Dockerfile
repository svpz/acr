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

RUN chmod -R 755 /app/staticfiles

# Expose the port Gunicorn will run on
EXPOSE 8000

# Run migrations, collect static files, and start Gunicorn after ensuring database is ready
CMD python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8000 api.wsgi:application