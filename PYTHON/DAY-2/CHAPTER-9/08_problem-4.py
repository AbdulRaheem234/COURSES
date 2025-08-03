with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\poems.txt") as f:
    content = f.read()
content = content.replace("Twinkle", "w8yrwjff")
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\poems.txt", "w") as f:
    f.write(content)    