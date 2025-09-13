FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install runtime dependencies only (avoid dev tools in final image)
RUN pip install --upgrade pip \
    && pip install fastapi uvicorn[standard] python-dotenv pyyaml httpx

# Copy application code and default configs
COPY app ./app
COPY configs ./configs

# Expose the default port
EXPOSE 8000

# Start the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
