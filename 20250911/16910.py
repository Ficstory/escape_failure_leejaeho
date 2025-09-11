"""
다시 말하자면, 
x2+y2<=N2인 격자점의 개수를 구하는 프로그램을 작성하라.
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    for i in range(-N,N+1):
        for j in range(-N,N+1):
            if (i**2) + (j**2) <= N**2:
                cnt += 1  
    print(f'#{tc} {cnt}')
