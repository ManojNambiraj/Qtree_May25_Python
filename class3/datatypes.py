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
    6. Membership OP
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

"""
    (True)  and (True)  ---> True
    (True)  and (False) ---> False
    (False) and (True)  ---> False
    (False) and (False) ---> False
"""

# or

"""
    (True)  or (True)  ---> True
    (True)  or (False) ---> True
    (False) or (True)  ---> True
    (False) or (False) ---> False
"""

# not

"""
    (True)  ---> False
    (False) ---> True
"""

# age = 22

# # result = (age > 18) and (age > 25)
# result = (age < 18) or (age > 25)

# print(not result)

# 7. Bitwise OP (&, |, ~, ^, <<, >>)

# &

    # 1 & 1 --> 1
    # 1 & 0 --> 0
    # 0 & 1 --> 0
    # 0 & 0 --> 0

a = 5
b = 3
result = a & b
print(result)

# Explanation

# (5) --> 00000101
# (3) --> 00000011
# -----------------
#         00000001  --> 1