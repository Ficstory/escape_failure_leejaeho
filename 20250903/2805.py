T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 가로세로 크기
    arr = [input() for _ in range(N)]
    # 농장 숫자 붙어있어서 걍 문자열로 받아옴
    M = (N - 1) // 2
    # 가로 N 세로 N 홀수 배열에서 가운데 인덱스

    arr_sum = 0
    # 합계

    # 우린 이제부터 가운데줄부터 그 위아래 줄 한줄씩 반복하면서 더해간다
    for i in range(M+1):
        # M은 가운데 줄 행 좌표이다.
        # M행의 위로 아래로 M개의 줄이 있다.
        # 그래서 위 아래 줄 같이 반복변수로 줄 i를 하나 설정해준다
        for j in range(i, N-i):
            # 한줄씩 올라갈/내려갈 때 마다 좌/우로 한칸씩 줄어든다
            # 그래서 반복을 할때 올라간 줄만큼 (양옆으로 빼주고 반복한다)
            if i == 0 :
                # 가운데 줄을 처음 계산할떄 위 아래 계산 로직 모두에 해당되므로 i가 0이면
                # 한번만 계산해준다
                arr_sum += int(arr[M-i][j])
            else:
                # 나머지는 가운데 기준 위로 i번째 줄, 아래로  i번째 줄을 더하면서 계산한다
                arr_sum += int(arr[M-i][j])
                arr_sum += int(arr[M+i][j])

    print(f'#{tc} {arr_sum}')



