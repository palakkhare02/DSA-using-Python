#### File Operation- Read And Write Files

# File handling is a crucial part of any programming language. Python provides built-in functions and methods to read from and write to files, both text and binary. This lesson will cover the basics of file handling, including reading and writing text files and binary files.
### Read a Whole File    
with open('example.txt','r') as file:
    content=file.read()
    print(content)
    
## Read a file line by line
with open('example.txt','r') as file:
    for line in file:
        print(line.strip()) ## sstrip() removes the newline character  

## Writing a file(Overwriting)

with open('example.txt','w') as file:
    file.write('Hello World!\n')
    file.write('this is a new line.')

## Write a file(wwithout Overwriting)
with open('example.txt','a') as file:
    file.write("Append operation taking place!\n")

### Writing a list of lines to a file
lines=['First line \n','Second line \n','Third line\n']
with open('example.txt','a') as file:
    file.writelines(lines)
