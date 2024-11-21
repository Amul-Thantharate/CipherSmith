# Build stage
FROM python:3.11-slim as builder

WORKDIR /app

# Copy all necessary files
COPY . .

# Install build dependencies and create virtual environment
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir .

# Final stage
FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Make sure we use the virtualenv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY app ./app

# Create a non-root user
RUN useradd -m appuser && \
    chown -R appuser:appuser /app
USER appuser

# Create directory for password storage
RUN mkdir -p /app/passwords && \
    chown -R appuser:appuser /app/passwords

# Command to run the application
ENTRYPOINT ["passforge"]
