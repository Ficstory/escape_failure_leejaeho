T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 각 숫자열의 길이
    N_arr = list(map(int,input().split()))
    M_arr = list(map(int,input().split()))
    # 각 숫자열

    max_val = 0
    # 최댓값 변수

    if N > M :
        # N의 길이가 M의 길이보다 큰 경우
        for i in range(N-M+1):
            # 큰배열의 인덱스를 옮겨줄 반복문
            current_sum = 0
            # 중간에 최댓값 기록할 변수
            for j in range(M):
                # 작은 배열의 길이만큼 반복
                current_sum += N_arr[i+j] * M_arr[j]
                # 곱해서 더해주고
            if current_sum > max_val :
                max_val = current_sum
                # 반복끝나면 최댓값과 비교하여 최신화

    elif M > N :
        # N의 길이가 M의 길이보다 큰 경우
        for i in range(M-N+1):
            current_sum = 0
            for j in range(N):
                # 작은 배열의 길이만큼 반복
                current_sum += M_arr[i+j] * N_arr[j]
            if current_sum > max_val :
                max_val = current_sum

    else:
        # 두개가 같은경우
        current_sum = 0
        for j in range(N):
            current_sum += N_arr[j] * M_arr[j]
        if current_sum > max_val:
            max_val = current_sum

    print(f'#{tc} {max_val}')




