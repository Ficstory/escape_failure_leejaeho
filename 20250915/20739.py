def J_find():
    # 세로탐색
    global max_len
    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
               cnt += 1
            elif arr[i][j] == 0:
                if cnt != 0:
                    if cnt > max_len:
                        max_len = cnt
                cnt = 0
        else:
            if cnt > max_len:
                max_len = cnt 
    
def i_find():
    # 가로탐색
    global max_len
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
               cnt += 1
               # 가로 반복돌다가 1이면 길이 +1
            elif arr[i][j] == 0:
                # 0을 만나면
                if cnt != 0:
                    # 카운트 숫자확인하고
                    if cnt > max_len:
                        max_len = cnt
                cnt = 0
                # 카운트 초기화
        else:
            if cnt > max_len:
                max_len = cnt 
            # 반복 다돌면 길이 비교
    

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0

    # 가로탐색
    i_find()
    # 세로탐색
    J_find()

    if max_len == 1:
        max_len = 0

    # 1인 경우 노이즈라서 0으로 함    
    print(f'#{tc} {max_len}')

