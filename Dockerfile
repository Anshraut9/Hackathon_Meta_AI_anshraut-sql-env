FROM python:3.10-slim

WORKDIR /app

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything
COPY . .

# Hugging Face Spaces uses port 7860 by default
EXPOSE 7860

# Run from the root so it can find 'server.app'
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]