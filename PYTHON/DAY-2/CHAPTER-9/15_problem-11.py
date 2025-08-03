import os

oldname = "C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\sample.txt"
newname = "C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\renamed_by_python.txt"
with open(oldname) as f:
    content = f.read()
with open(newname, "w") as f:
    f.write(content)
os.remove(oldname)
