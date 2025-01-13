import math

N = int(input())
appliers = list(map(int, input().split()))
B, C = list(map(int, input().split()))

main = 0
sub = 0


for a in appliers:
    mainDiff = a - B
    main += 1
    if mainDiff > 0:
        subCount = math.ceil(mainDiff / C)

        sub += subCount

print(main + sub)
