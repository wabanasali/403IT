import math
def solution(s_str):
    l,r = [x for x in s_str],-1
    if len(l) == 0:
        r = 0
    else:
        if len(l)%2 == 1 and len(l) > 2:
            l1 = l[:len(l)//2]
            l2 = l[math.ceil(len(l)/2):]
            l2.reverse()
            if l1 == l2:
                r = len(l)//2
    return r

print(solution('racecar'))