for i in range(2, 21):
    with open(f"C:\\Users\\Admin\\OneDrive\\Desktop\\COURSES\\PYTHON\\DAY-2\\CHAPTER-9\\tables\\Multiplication_table_of_{i}", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i*j}\n")
    break
