#https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    start = 0
    end = len(people)-1
    
    while start <= end:
        answer += 1
        if start == end :
            break
        if people[start]+people[end] <=limit:
            start += 1
            end -=1
        else :
            start +=1

    return answer
