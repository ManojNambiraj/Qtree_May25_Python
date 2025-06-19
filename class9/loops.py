# Looping ( DRY --> Dont repeat your code )

# for loop

    # Example: 1

        # for i in range(1, 11):
        #     print(i)

    # Example: 2

        # fruits = ["apple", "banana", "orange", "grapes", "kiwi", "watermelon"]

        # for item in fruits:
        #     print(item)

# while loop

    # a = 1

    # while a <= 10:
    #     print(a)
    #     a += 1
    # else:
    #     print("a is no longer less than 10")

# Jumping statements

    # break

i = 1

while i < 6:
    print(i)
    if(i == 3):
        break
    i += 1

    # continue

        # i = 0

        # while i <= 5:
        #     i += 1
        #     if(i == 3):
        #         continue
        #     print(i)