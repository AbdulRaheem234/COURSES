with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\this.txt") as f:
    content = f.read()

with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\copy.txt", 'w') as f:
    f.write(content)
