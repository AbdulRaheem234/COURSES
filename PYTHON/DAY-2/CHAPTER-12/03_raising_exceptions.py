def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Harry")

a = increment('364')
print(a)