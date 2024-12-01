# Use the official Python image as the base
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the app
CMD ["python", "app.py"]

