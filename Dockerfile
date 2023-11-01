FROM python:3.11

# Install dependencies
RUN apt-get update && \
    apt-get install -y curl gnupg lsb-release && \
    rm -rf /var/lib/apt/lists/*

# Install ODBC driver dependencies
RUN apt-get update && \
    apt-get install -y gnupg && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | tee /etc/apt/sources.list.d/msprod.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y mssql-tools unixodbc-dev

# Set environment variables
ENV PATH="/opt/mssql-tools/bin:${PATH}"

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


# Make port 80 available to the world outside this container
EXPOSE 80

CMD ["/bin/bash", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 && /opt/mssql-tools/bin/sqlcmd -S db -U sa -P StrongPassword!123 -d master -i /docker_setup.sql"]
