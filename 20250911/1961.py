"""
N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도,
270도 회전한 모양을 출력하라.


[제약 사항]
N은 3 이상 7 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고,
그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N이 주어지고,
다음 N 줄에는 N x N 행렬이 주어진다.

[출력]

출력의 첫 줄은 '#t'로 시작하고,

다음 N줄에 걸쳐서 90도, 180도, 270도 회전한 모양을 출력한다.

입력과는 달리 출력에서는 회전한 모양 사이에만 공백이 존재함에 유의하라.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""
import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    turn_90 = [[0] * N for _ in range(N)]
    turn_180 = [[0] * N for _ in range(N)]
    turn_270 = [[0] * N for _ in range(N)]
    # 돌린 결과물을 담아줄 각각의 빈배열 만들어줌

    # 90도 돌리는것은 왼쪽에서 오른쪽으로 가며 아래에서 위로 반복해주면 됨
    # 180도 돌리는것은 아래에서 위로 가며 오른쪽에서 왼쪽으로 반복해주면 됨
    # 270도 돌리는것은 왼쪽에서 오른쪽으로 가며 위에서 아래로 반복해주면 됨
    # 각각의 결과물을 한땀 한땀 리스트에 넣어서 완성해줌

    c = 0
    for j in range(N):
        d = 0
        for i in range(N-1, -1, -1):
            turn_90[c][d] = arr[i][j]
            d += 1
        else:
            c+=1

    c = 0
    for i in range(N - 1, -1, -1):
        d = 0
        for j in range(N-1, -1, -1):
            turn_180[c][d] = arr[i][j]
            d += 1
        else:
            c+=1

    c = 0
    for j in range(N - 1, -1, -1):
        d = 0
        for i in range(N):
            turn_270[c][d] = arr[i][j]
            d += 1
        else:
            c+=1

    # 출력방식 고려하여
    print(f'#{tc}')
    for i in range(N):
        print(f'{"".join(map(str, turn_90[i]))} {"".join(map(str, turn_180[i]))} {"".join(map(str, turn_270[i]))}')
    # 위에 한줄씩 출력하고 반복으로 N줄 출력함