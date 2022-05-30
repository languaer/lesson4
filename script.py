Lesson_4_1

def revers(n):
    if len(n) == 1:
        return n
    return n[-1] + revers(n[:-1])

x = revers(input())
print(x)
