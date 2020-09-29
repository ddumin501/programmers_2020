#https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    bridge = []
    total_weight, time = 0, 0
    while truck_weights or bridge:
        time +=1
        if bridge and time - bridge[0][1] ==  bridge_length:
                total_weight -= bridge[0][0]
                bridge.pop(0)
        if truck_weights and total_weight + truck_weights[0] <= weight:
                total_weight += truck_weights[0]
                bridge.append((truck_weights.pop(0),time))
            
    return time
