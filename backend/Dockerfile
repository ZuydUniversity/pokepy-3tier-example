FROM python:3.12-alpine

# Install MariaDB client libs and gcc
RUN apk add --no-cache mariadb-connector-c mariadb-connector-c-dev gcc musl-dev

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt /app/
RUN pip install --prefer-binary --no-cache-dir --upgrade -r requirements.txt

# Copy app code
COPY . /app/

EXPOSE 80

# Run FastAPI app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
