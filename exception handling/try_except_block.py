## Exception try ,except block

try:
    a=b
except:
    print("The variable has not been assigned")

    # output The variable has not been assigned

## try,except,else and finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
except Exception as ex:
    print(ex)
else:
    print(f"The result is {result}")
finally:
    print("Execution complete.")

