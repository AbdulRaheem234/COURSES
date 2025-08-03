f = open('C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\poems.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")    
f.close()