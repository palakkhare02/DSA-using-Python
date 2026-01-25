### Binary Files

# Writing to a binary file
data = b'\x00\x01\x02\x03\x04'
with open('example.bin', 'wb') as file:
    file.write(data)

# Reading a binary file
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content) # output b'\x00\x01\x02\x03\x04'
