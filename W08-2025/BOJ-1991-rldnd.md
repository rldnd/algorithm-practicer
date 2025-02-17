# [[BOJ] 트리 순회](https://www.acmicpc.net/problem/1991)

> [트리] [재귀]

## 발상

- 재귀 방식으로 루트의 위치에 따라 재귀함수 호출 방식을 바꾸자

## <br>정답 코드

```python
import sys
readline = sys.stdin.readline

N = int(readline())
tree = {}
EMPTY = '.'

for _ in range(N):
    row = readline().split()
    tree[row[0]] = row[1:]

def preorder(point):
    print(point, end='')
    if not tree[point][0] == EMPTY:
        preorder(tree[point][0])
    if not tree[point][1] == EMPTY:
        preorder(tree[point][1])

def inorder(point):
    if not tree[point][0] == EMPTY:
        inorder(tree[point][0])
    print(point, end='')
    if not tree[point][1] == EMPTY:
        inorder(tree[point][1])

def postorder(point):
    if not tree[point][0] == EMPTY:
        postorder(tree[point][0])
    if not tree[point][1] == EMPTY:
        postorder(tree[point][1])
    print(point, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
```
