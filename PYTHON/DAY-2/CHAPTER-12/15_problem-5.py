num = int(input("Enter your number: "))

table = [num*i for i in range(1, 11)]
print(table)
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-12\\tables.txt", "a") as f:
    f.write(str(table))
    f.write('\n')