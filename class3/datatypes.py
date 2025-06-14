# Datatypes:

    # # a = 10           # integer (numbers)
    # # a = 10.5         # float
    # # a = 'Ram'        # string (Text)
    # # a = False        # boolean

    # print(a)
    # print(type(a))

# Operators:

"""
    1. Arithmetic OP
        (+, -, *, /, %, **, //)

    2. Assignment OP
        (=, +=, -=, *=, /=, %=, **=, //=)    
    
    3. Comparison OP
        (==, !=, <, >, <=, >=)
    
    4. Logical OP
        (and, or, not)
    
    5. Identity OP
        (is, is not)

    6. Membership OP
        (in, not in)

    7. Bitwise OP
        (&, |, ~, ^, <<, >>)

"""

# 1. Arithmetic OP:  (+, -, *, /, %, **, //)

    # a = 10
    # b = 7

    # result = a + b
    # result = a - b
    # result = a * b
    # result = a / b
    # result = a % b
    # result = a ** b
    # result = a // b

    # print(result)

# 2. Assignment OP  (=, +=, -=, *=, /=, %=, **=, //=)

    # a = 5

    # a += 200    # a = a + 200

    # print(a)

# 3. Comparison OP (==, !=, <, >, <=, >=) --> Boolean (True or False)

    # age = 18

    # result = (age == 18)
    # result = (age != 18)
    # result = (age < 18)
    # result = (age > 18)
    # result = (age <= 18)
    # result = (age >= 18)

    # print(result)

# 4. Logical OP (and, or, not)

    # and

    # """
    #     (True)  and (True)  ---> True
    #     (True)  and (False) ---> False
    #     (False) and (True)  ---> False
    #     (False) and (False) ---> False
    # """

    # or

    # """
    #     (True)  or (True)  ---> True
    #     (True)  or (False) ---> True
    #     (False) or (True)  ---> True
    #     (False) or (False) ---> False
    # """

    # not

    # """
    #     (True)  ---> False
    #     (False) ---> True
    # """

    # age = 22

    # # result = (age > 18) and (age > 25)
    # result = (age < 18) or (age > 25)

    # print(not result)

# 7. Bitwise OP (&, |, ~, ^, <<, >>)

    # & --> (Bitwise AND)

        # 1 & 1 --> 1
        # 1 & 0 --> 0
        # 0 & 1 --> 0
        # 0 & 0 --> 0

    # | --> (Bitwise OR)

        # 1 | 1 --> 1
        # 1 | 0 --> 1
        # 0 | 1 --> 1
        # 0 | 0 --> 0

    # ^ --> (Bitwise XOR)

        # 1 | 1 --> 0
        # 1 | 0 --> 1
        # 0 | 1 --> 1
        # 0 | 0 --> 0

        # a = 5

        # result = a << 2

        # print(result)

        # Explanation

        # (5) --> 00000101
        # -----------------
        # (1) --> 00001010     --> 10
        # (2) --> 00010100     --> 20

# 5. Identity OP --> (is, is not)

    # x = ["apple", "banana", "grapes"]
    # y = ["apple", "banana", "grapes"]
    # z = x

    # print(x is z)
    # print(x is not z)

# 6. Membership OP --> (in, not in)

    # x = ["apple", "banana", "grapes"]

    # print("apple" not in x)