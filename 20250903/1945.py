"""
숫자 N은 아래와 같다.

N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e 를 출력하라.
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    a = 0
    # 소인수 2의 수
    b = 0
    # 소인수 3의 수
    c = 0
    # 소인수 5의 수
    d = 0
    # 소인수 7의 수
    e = 0
    # 소인수 11의 수

    while True:
        if N % 2 == 0:
            a += 1
            N = N//2
        elif N % 2 != 0:
            break
        # 2로 나눠질때까지 나누고 나눌때마다 a+1

    while True:
        if N % 3 == 0:
            b += 1
            N = N//3
        elif N % 3 != 0:
            break
        # 3로 나눠질때까지 나누고 나눌때마다 b+1

    while True:
        if N % 5 == 0:
            c += 1
            N = N//5
        elif N % 5 != 0:
            break
        # 5로 나눠질때까지 나누고 나눌때마다 c+1

    while True:
        if N % 7 == 0:
            d += 1
            N = N//7
        elif N % 7 != 0:
            break
        # 7로 나눠질때까지 나누고 나눌때마다 d+1

    while True:
        if N % 11 == 0:
            e += 1
            N = N // 11
        elif N % 11 != 0:
            break
        # 11로 나눠질때까지 나누고 나눌때마다 e+1

    print(f'#{tc} {a} {b} {c} {d} {e}')



