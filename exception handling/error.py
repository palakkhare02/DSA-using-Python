try:
    result=1/0
except ZeroDivisionError as ex:
    print(ex)
    print("Please enter the denominator greater than 0")
# output :
# division by zero
# Please enter the denominator greater than 0


try:
    num=int(input("Enter a number"))
    result=10/num
except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("enter denominator greater than 0")
except Exception as ex:
    print(ex)
    

### File handling and Exception HAndling

try:
    file=open('example1.txt','r')
    content=file.read()
    a=b
    print(content)

except FileNotFoundError:
    print("The file does not exists")
except Exception as ex:
    print(ex)

finally:
    if 'file' in locals() or not file.closed():
        file.close()
        print('file close') 

# output name 'b' is not defined
# file close           