### Writing and then reading a file

with open('example.txt','w+') as file:
    file.write("Hello world\n")
    file.write("This is a new line \n")

    ## Move the file cursor to the beginning
    file.seek(0)

    ## Read the content of the file
    content=file.read()
    print(content)


The w+ mode in Python is used to open a file for both reading and writing. If the file does not exist, it will be created. If the file exists, its content is truncated (i.e., the file is overwritten).
