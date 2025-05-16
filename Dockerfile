# Use a slim Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your code into the container
COPY . .

# Install required packages
RUN pip install --no-cache-dir fastapi uvicorn openai python-dotenv

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
