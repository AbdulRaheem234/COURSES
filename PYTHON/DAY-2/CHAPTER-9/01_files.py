# f = open('C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\sample.txt', 'r')
# data = f.read()

f = open('C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\sample.txt', 'r')
# reads first 5 characters from the file
data = f.read(578)
print(data)
f.close()