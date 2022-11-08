def solution(total):
    hours = total//60%24
    mins = total%60
    return f'{hours} {mins}'
