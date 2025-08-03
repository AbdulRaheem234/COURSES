content = True
i = 1
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\log.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print("Yes python is present on line number: {i}")
    i += 1
