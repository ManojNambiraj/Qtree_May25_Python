# File handling

# Read:

    # file = open(r"C:\Users\Manoj\OneDrive\Desktop\CourseFiles\demo.txt", 'r')

    # content = file.read()

    # print(content)

# Write:

    # a -> append

        # file = open("demo.txt", 'a')

        # file.write("\n I have add a more content")

    # w -> write

        # file = open("demo.txt", 'w')

        # file.write("I will delete the existing contents")

# Create:

file = open("newfile.txt", 'x')

print(file)