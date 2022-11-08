def solution(n):
    str1 = '   _~_   '
    str2 = '  (o o)  '
    str3 = ' /  V  \\ '
    str4 = '/(  _  )\\'
    str5 = '  ^^ ^^  '
    endl = '\n'
    if n == 0:
        return ''
    return str1*n + endl + str2*n + endl + str3*n + endl + str4*n + endl + str5*n 
