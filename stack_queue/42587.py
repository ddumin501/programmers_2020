#https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque(priorities)
    
    while dq:
        p = dq.popleft()
        
        if len(dq)==0:
            return answer +1
        
        if p >= max(dq):
            answer += 1
            if location == 0:
                return answer
            location -=1
            
        else :
            dq.append(p)
            if location == 0:
                location = len(dq)-1
            else : 
                location-=1
    return answer
