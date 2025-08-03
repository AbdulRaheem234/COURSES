with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes python is present")
else:
    print("No python is not present")
