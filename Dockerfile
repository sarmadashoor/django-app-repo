# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /django

# Copy the requirements file into the container at /django
COPY requirements.txt /django/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /django
COPY . /django/

# Make wait-for-it.sh executable
RUN chmod +x /django/wait-for-it.sh

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the wait-for-it.sh script and then start the Django server
CMD ["./wait-for-it.sh", "postgres:5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
