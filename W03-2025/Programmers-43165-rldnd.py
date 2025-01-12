def dfs(numbers, value, target, answer):
    if len(numbers) == 1:
        for mul in [-1, 1]:
            if target == (value + (numbers[0] * mul)):
                answer[0] += 1
        return
        
    for mul in [-1, 1]:
        dfs(numbers[1:], value + (numbers[0] * mul), target, answer)
        

def solution(numbers, target):
    answer = [0]
    dfs(numbers, 0, target, answer)
    
    return answer[0]
