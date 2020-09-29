#https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    
    def dfs(index, total):
        if index == n:
            if total == target:
                nonlocal answer
                answer +=1
            return
        
        
        dfs(index+1,total+numbers[index])
        dfs(index+1,total-numbers[index])
    
    dfs(0,0) 
    return answer
