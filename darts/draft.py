def score(x, y):
    if x in range(0, 2):
        if y <= 1:
            return 10
        elif y <= 5:
            return 5
        elif y <= 10:
            return 1
        else:
            return 0
    if x in range(2, 6):
        if 2 <= y <= 5:
            return 5
        elif 6 <= y <= 10:
            return 1
        else:
            return 0
    if x in range(6, 11):
        if 6 <= y <= 10:
            return 1
    return 0

def score2(x, y):
    distance = (x**2 + y**2)**0.5

    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0