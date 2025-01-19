# [[BOJ] 잃어버린 괄호](https://www.acmicpc.net/problem/1541)

> [수학] [문자열] [파싱]

## 발상

- 최소의 값을 만들기 위해 -, + 가 둘 다 존재하는 경우에 +로 큰 값을 만들고 - 를 해주면 최소의 값을 만들 수 있다

## <br>[Optional] 틀린 풀이 코드 및 틀린 이유

> 처음에 데이터 처리를 잘못해서 틀렸는데 수학적으로 생각해서 문제를 풀어본 뒤 코드에 적용해서 맞을 수 있었다. 

```python
import sys
readline = sys.stdin.readline
from collections import deque

queue = deque()

input_sen = readline().split('-')


re = 0
if(len(input_sen)==1):
    plus_only = input_sen[0].split('+')
    for i in range(len(plus_only)):
        re += int(plus_only[i])
    print(re)
    sys.exit(0)


for i in range(len(input_sen)):
    if "+" in input_sen[i]:
        plus = input_sen[i].split('+')
        for k in range(0, len(plus)-1,2):
            # 이 부분이 틀렸음. 더하는 숫자의 갯수가 짝수라고만 생각.
            queue.append(int(plus[k])+int(plus[k+1]))
    else:
        queue.append(int(input_sen[i]))
   
re = queue[0]


for i in range(1, len(queue)):
        re -= queue[i]
    
print(re) 
```

## <br>정답 코드

- 데이터 처리하는 부분만 고치니 맞았다.

```python
import sys
readline = sys.stdin.readline
from collections import deque

queue = deque()

input_sen = readline().split('-')


re = 0
if(len(input_sen)==1):
    plus_only = input_sen[0].split('+')
    for i in range(len(plus_only)):
        re += int(plus_only[i])
    print(re)
    sys.exit(0)


for i in range(len(input_sen)):
    if "+" in input_sen[i]:
        plus = input_sen[i].split('+')
        plus_re = 0
        for k in range(len(plus)):
            plus_re += int(plus[k])
        queue.append(plus_re)
    else:
        queue.append(int(input_sen[i]))
   
re = queue[0]


for i in range(1, len(queue)):
        re -= queue[i]
    
print(re) 
```