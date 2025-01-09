import sys
readline = sys.stdin.readline

N = int(readline())

five = N // 5

while five >= 0:
    if not (N - five * 5) % 3:
        print(five + (N - five * 5) // 3)
        break
    else:
        five -= 1
        
if five < 0:
    print(-1)