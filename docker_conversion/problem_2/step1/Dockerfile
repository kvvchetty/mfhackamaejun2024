# Use a slim Python 3.12 image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Copy your application code
COPY . .


# ... other instructions ...

# Mount the local directory as a volume
VOLUME ["/app/input", "/app/output"]

# Define command to run with arguments
ENTRYPOINT ["python","./p2step1.py"]
# Optional: Set environment variables
# ENV MY_VAR="some_value"
