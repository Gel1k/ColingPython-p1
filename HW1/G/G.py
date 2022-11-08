def solution(a, b):
    for i in b:
        if i not in a:
            j = 0
            while j < b.count(i):
                j+=1
                a.append(i)
    return sorted(a)
