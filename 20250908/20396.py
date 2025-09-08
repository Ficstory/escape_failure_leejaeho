"""
뒤집기는 i번째부터 j개의 돌을 i번째 돌의 색으로 바꿔놓는다.
뒤집기는 가능한 돌에 대해서만 진행한다.

"""
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N = 돌의 개수
    # M = 뒤집기 반복 횟수
    stones = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        # m만큼 뒤집기 반복이 이루어지므로 반복문 인풋을 받아온다
        for k in range(i-1, i+j-1):
            # i 번째 돌 = 인덱스로 찾으려면 -1 해줘야함
            # i 번째 돌부터 j개의 돌이므로 i+j-1까지 
            if k < N:
                # 인덱스에러가 나지 않도록 N보다 작을때
                stones[k] = stones[i-1]
                # i번째 돌의 색깔로 다 바꾼다
            else:
                break

    print(f'#{tc} {" ".join(map(str, stones))}')
    # 리스트 벗겨서 문자열로 출력