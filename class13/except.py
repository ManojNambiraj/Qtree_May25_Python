# Exception Handling:

try:
    x = 4

    result = x/0

    print(result)

except ZeroDivisionError:

    print("It's a ZeroDivisionError")

except:

    print("Something went wrong...!")