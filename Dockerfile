# Use Ubuntu as the base image
FROM ubuntu:latest

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /home

# Copy the python script into the container
COPY script.py /home/script.py

# Create directories
RUN mkdir data output

# Copy the two text files into the container (must be in the same directory as the dockerfile)
COPY IF.txt /home/data/IF.txt
COPY Limerick-1.txt /home/data/Limerick-1.txt

# Command to run the script
CMD python3 script.py