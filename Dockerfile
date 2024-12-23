FROM python:3.10

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV PROJECT_ID="account-pocs"
ENV LOCATION="global"
ENV DATASTORE_ID="starhub-faq-ds-search_1723603291738"
ENV AGENT_APPLICATION_ID="starhub-faq-app_1723603258721"

# Expose the application port
EXPOSE 8000

# Start the application
CMD ["fastapi","run"]
