#https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    index =0
    count = 0
    
    answer = []
    
    while index <len(speeds):
        for i in range(index, len(speeds)):
            progresses[i]+=speeds[i]
            
        for i in range(index,len(speeds)):
            if progresses[i]>=100:
                index = i+1
                count +=1
                print(count)
            else:
                if count>0:
                    answer.append(count)
                count = 0
                break
    answer.append(count)
            
    return answer
