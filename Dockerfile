# Multi-stage build (decreases image size)

# Build stage
FROM python:3.10-slim as builder

# Set working directory in the build stage
WORKDIR /app

# Copy requirements.txt and install dependencies into wheels
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# Copy the rest of the application code
COPY . .

# Final stage
FROM python:3.10-slim

# Set working directory in the final stage
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app/wheels /app/wheels
COPY --from=builder /app /app

# Install dependencies from pre-built wheels
RUN pip install --no-cache-dir --no-index --find-links=/app/wheels -r requirements.txt

# Clean up unnecessary files
RUN rm -rf /app/wheels

# Define environment variable to ensure Python outputs everything to the console
ENV PYTHONUNBUFFERED=1

# Run the application
CMD ["python", "main.py"]