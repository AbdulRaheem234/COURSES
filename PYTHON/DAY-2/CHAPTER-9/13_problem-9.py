file1 = "C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\log.txt"
file2 = "C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\this.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()
if f1 == f2:
    print("Files are identical:")
else:
    print("Files are not identical:")                