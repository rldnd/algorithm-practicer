# 스택 (Stack)

- 한쪽에서만 자료를 넣고 뺄 수 있는 LIFO(Last In First Out) 형식의 선형 자료구조

## 예시

```python
stack = []

stack.append(1) # [1]
stack.append(2) # [1,2]
stack.append(3) # [1,2,3]

stack.pop() # [1,2]
stack.pop() # [1]
stack.pop() # []
```

# 큐 (Queue)

- 한쪽으로 삽입하고, 다른 한 쪽으로 삭제하는 FIFO(First In First Out) 형식의 선형 자료구조

## 관련 용어

- **프런트(front)** : 삭제 연산이 수행되는 위치
- **리어(rear)** : 삽입 연산이 수행되는 위치
- **디큐(dnQueue)** : 프런트에서 이뤄지는 삭제 연산
- **인큐(enQueue)** : 리어에서 이뤄지는 삽입 연산

## 예시

```python
from collections import deque

queue = deque()

queue.append(1) # [1]
queue.append(2) # [1,2]
queue.append(3) # [1,2,3]

queue.popleft() # [2,3]
queue.popleft() # [3]
queue.popleft() # []
```

# 덱 (Dequeue)

- 양쪽에서 삽입과 삭제가 가능한 자료구조

## 예시

```python
from collections import deque

queue = deque()

queue.append(1) # [1]
queue.append(2) # [1,2]
queue.append(3) # [1,2,3]

queue.pop() # [1,2]
queue.popleft() # [2]
queue.pop() # []
```
