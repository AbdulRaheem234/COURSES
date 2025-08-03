n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\PYTHON\\CHAPTER-12\\tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")