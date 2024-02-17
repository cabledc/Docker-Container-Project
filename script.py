import os
from collections import Counter

# Define the directories
data_dir = "/home/data"
output_dir = "/home/output"
result_file = os.path.join(output_dir, "result.txt")

# List all text files in data directory
text_files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]

# Function to count words in a file
def count_words_in_file(filepath):
    with open(filepath, 'r') as file:
        words = file.read().split()
        return len(words), Counter(words)

# Calculate the total number of words and top 3 words in IF.txt
total_words = 0
top_words = None
for file in text_files:
    filepath = os.path.join(data_dir, file)
    word_count, word_counter = count_words_in_file(filepath)
    total_words += word_count
    if file == "IF.txt":
        top_words = word_counter.most_common(3)

# Find the IP address of the machine
ip_address = os.popen('hostname -I').read().strip()

# Write the results to a file
with open(result_file, 'w') as file:
    file.write(f"List of text files: {', '.join(text_files)}\n")
    file.write(f"Total number of words in both files: {total_words}\n")
    file.write(f"Top 3 words in IF.txt: {top_words}\n")
    file.write(f"IP address of the machine: {ip_address}\n")

# Print the results
print(open(result_file).read())