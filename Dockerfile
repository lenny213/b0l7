# Use an official Python runtime as a base image
FROM python:latest

#set Maintainer
LABEL maintainer "g.ribarski@gmail.com"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# set HealthCheck
# HEALTHCHECK --interval=5s \
#             --timeout=5s \
#             CMD curl -f http://127.0.0.1:10100 || exit 1

# Make port 80 available to the world outside this container
EXPOSE 10100

# Run app.py when the container launches
CMD ["python", "main.py"]
