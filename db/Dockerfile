FROM mariadb:latest

# Optional: document defaults (actual values still come from env vars)
ENV MYSQL_DATABASE=pokemon \
    MYSQL_USER=user \
    MYSQL_ROOT_PASSWORD=rootpassword \
    MYSQL_PASSWORD=password

# Copy initialization SQL
# This is only executed on first startup when /var/lib/mysql is empty
COPY init.sql /docker-entrypoint-initdb.d/init.sql

# Expose MariaDB port (documentation only)
EXPOSE 3306
