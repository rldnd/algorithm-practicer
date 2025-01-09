import sys
readline = sys.stdin.readline

N = int(readline())
S = [list(map(int, readline().split())) for _ in range(N)]

# 이거 itertools 쓰면 되긴 함
def combination(lst, n):
    answer = []
    if n == 0:
        return []
    if n == 1:
        return [[i] for i in lst]
    for i in range(len(lst)):
        element = lst[i]
        rest = combination(lst[i+1:], n-1)
        for item in rest:
            answer.append([element] + item)
    return answer

s_combination = combination([i for i in range(N)], N // 2)

minimum = 1e9

for combs in s_combination:
    combs_count, rest_count = 0, 0
    rest = list(set([i for i in range(N)]) - set(combs))
    
    combs_two_combs = combination(combs, 2)
    rest_two_combs = combination(rest, 2)
    
    for i in range(len(combs_two_combs)):
        [a, b] = combs_two_combs[i]
        [c, d] = rest_two_combs[i]
        combs_count += S[a][b]
        combs_count += S[b][a]
        rest_count += S[c][d]
        rest_count += S[d][c]
    minimum = min(minimum, abs(combs_count - rest_count))

print(minimum)