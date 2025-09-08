"""
동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고,
게임의 규칙은 다음과 같다.

i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해,
각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
주어진 돌을 벗어나는 경우 뒤집기는 중지된다.

"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N = 돌 갯수
    # M = 뒤집는 횟수
    stones = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        # m만큼 뒤집는 것이 이루어지므로 반복문안에서 받아와준다 
        for k in range(1, j+1):
            # 마주보는 j개의 돌에 대해 적용되어야 하므로 
            # i를 중심으로 j개의 돌까지 나아가도록 설정 
            if i-k-1 >= 0 and i+k-1 < N:
                # 나아가다가 범위를 벗어나면 작동되지 않도록 함
                if stones[i+k-1] == stones[i-k-1]:
                    # 애초에 i번째 돌이 인덱스로는 i-1이므로
                    # i-1을 중심으로 좌, 우를 비교해야함
                    if stones[i+k-1] == 1:
                        # 1일때는 뒤집어서 0으로 바꿔주고
                        stones[i+k-1] = 0
                        stones[i-k-1] = 0

                    elif stones[i+k-1] == 0:
                        # 0일때는 뒤집어서 1로 바꿔줌
                        stones[i+k-1] = 1
                        stones[i-k-1] = 1

    print(f'#{tc} {" ".join(map(str, stones))}')
    # 출력