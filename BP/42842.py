#https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    xy = yellow+brown
    array = []
    for i in range(1,(brown+1)//2):
        if xy%i==0:
            a = max(xy//i,i)
            b = min(xy//i,i)
            array.append((a,b))
    
    answer = []
    for a,b in array:
        if a+b == ((brown+4)//2):
            answer = [a,b]

    return answer
