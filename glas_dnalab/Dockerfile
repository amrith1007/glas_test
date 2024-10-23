# Use an official MySQL image as a base image
FROM mysql:latest

# Copy the SQL file containing your specific database model to the container
COPY ./src/glas/database/setup/schema.sql /docker-entrypoint-initdb.d/

# This port can be something else if needed
EXPOSE 3306