FROM python:3.9-slim

# Set the working directory
WORKDIR /home

COPY script.py /home/script.py

# Create the directories for the data and the output
RUN mkdir data output

# Copy text files into the container
COPY IF.txt ./data/IF.txt
COPY Limerick-1.txt ./data/Limerick-1.txt

# Command to run the script
CMD python3 script.py
