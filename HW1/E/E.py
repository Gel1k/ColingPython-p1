def solution(x1, y1, x2, y2):
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 and (x1 != x2 or y1 != y2):
        return True
    return False
