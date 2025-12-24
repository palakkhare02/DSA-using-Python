### Read the content froma  source text fiile and write to a destination text file
# Copying a text file
with open('example.txt', 'r') as source_file:
    content = source_file.read()

with open('destination.txt', 'w') as destination_file:
    destination_file.write(content)