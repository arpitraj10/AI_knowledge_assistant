# Use stable Python (NOT 3.13)
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list first (for Docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy backend source code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start backend server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
