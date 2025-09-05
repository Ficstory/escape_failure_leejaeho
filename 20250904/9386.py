T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Nums = input()
    #문자열로 받아옴

    max_count = 1
    # 최소값은 1
    count = 1
    # 연속된 숫자 확인하는 변수를 1로 초기화 
    for i in range(N-1):
        # 인덱스로 반복
        if Nums[i] == '1':
            # 1이 맞으면
            if Nums[i] == Nums[i+1]:
                count += 1
                # 그 다음 인덱스가 같은지 확인하고 맞으면 카운트 +1
                if count > max_count:
                    max_count = count
                    # 최댓값 비교
        elif Nums[i] == '0':
            count = 1
            # 0이 나오면 다시 초기화

    print(f'#{tc} {max_count}')