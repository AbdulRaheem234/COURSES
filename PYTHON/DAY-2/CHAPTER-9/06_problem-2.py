def game():
    return 44690780


score = game()
with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\hiscore.txt")as f:
    hiScoreStr = int(f.read())
if int(hiScoreStr) < score or hiScoreStr == '':
    with open("C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\hiscore.txt", "w") as f:
        f.write(str(score))
