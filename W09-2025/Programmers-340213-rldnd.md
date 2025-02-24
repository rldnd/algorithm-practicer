# [[Programmers] [PCCP 기출문제] 1번 / 동ㅕ상 재생기](https://school.programmers.co.kr/learn/courses/30/lessons/340213?language=python3#)

## 발상

- 단순 구현 문제

## <br>정답 코드

```python
def get_min_sec(str):
    time = {}
    time['min'] = int(str[:2])
    time['sec'] = int(str[3:])
    return time

def min_sec_to_string(time):
    minute = str(time['min']).rjust(2, '0')
    second = str(time['sec']).rjust(2, '0')
    return f'{minute}:{second}'

def handle_next(time, end_time):
    res = time.copy()
    if res['sec'] >= 50:
        res['min'] = res['min'] + 1
        res['sec'] = res['sec'] - 50
    else:
        res['sec'] = res['sec'] + 10
    if res['min'] > end_time['min'] or (res['min'] == end_time['min'] and res['sec'] > end_time['sec']):
        return end_time.copy()
    return res

def handle_prev(time):
    res = time.copy()
    if res['sec'] < 10:
        if res['min'] == 0:
            res['sec'] = 0
        else:
            res['min'] = res['min'] - 1
            res['sec'] = 60 - (10 - res['sec'])
    else:
        res['sec'] = res['sec'] - 10
    return res

def handle_op(time, op_start, op_end):
    if (op_start['min'] < time['min'] or (op_start['min'] == time['min'] and op_start['sec'] <= time['sec'])) and (op_end['min'] > time['min'] or (op_end['min'] == time['min'] and op_end['sec'] >= time['sec'])):
        return op_end.copy()
    return time

def solution(video_len, pos, op_start, op_end, commands):
    video_len = get_min_sec(video_len)
    pos = get_min_sec(pos)
    op_start = get_min_sec(op_start)
    op_end = get_min_sec(op_end)

    for com in commands:
        pos = handle_op(pos, op_start, op_end)
        if com == 'next':
            pos = handle_next(pos, video_len)
        if com == 'prev':
            pos = handle_prev(pos)
        pos = handle_op(pos, op_start, op_end)

    return min_sec_to_string(pos)
```
