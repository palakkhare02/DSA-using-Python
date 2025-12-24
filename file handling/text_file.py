### write in a file

# with open('example.txt','w') as file:
#     content=file.write("hey! good morning...keep growing day by day")

### Read a Whole File    
# with open('example.txt','r') as file:
#     content=file.read()
#     print(content) 
## Read a file line by line
with open('example.txt','r') as file:
    for line in file:
        print(line.strip()) ## sstrip() removes the newline character       