words = ["above", "world", "high"]

with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\poems.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "w8yrwjff")

with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\poems.txt", "w") as f:
    f.write(content)
