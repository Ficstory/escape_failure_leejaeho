T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrot = list(map(int, input().split()))

    max_count = 1
    # 연속된 기본 값을 1로 정했기 때문에 최댓값도 1
    bigger_count = 1
    # 연속된 기본값을 1로 초기화
    for i in range(N-1):
        if carrot[i] < carrot[i+1]:
            bigger_count += 1
            # 당근이 커지면 카운트 +
            if max_count < bigger_count:
                max_count = bigger_count
                # 커질때 마다 최댓값 확인 
        elif carrot[i] >= carrot[i+1]:
            bigger_count = 1
            # 작아지면 카운트 초기화
        
    print(f'#{tc} {max_count}')


