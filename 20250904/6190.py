
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    nums = list(map(int, input().split()))

    max_danjo = -1
    # 최댓값을 -1로 잡아서
    # 만약 단조 값이 없으면 초기값을 출력하도록 함
    for i in range(N):
        for j in range(i+1,N):
            danjoni = nums[i] * nums[j]
            # 인덱스를 기준으로 곱하고
            str_danjoni = str(danjoni)
            # 곱해진 값이 계속 증가하는 수 임을 확인하기 위해 문자열로 변경
            for c in range(len(str_danjoni)-1):
                if str_danjoni[c] > str_danjoni[c+1]:
                   # 증가하는 것이 멈추면 반복문도 중간에 중단
                   # *문자열이라도 숫자끼리 비교하면 비교가능
                   break                
            else:
                if danjoni > max_danjo:
                    max_danjo = danjoni
                    # 반복문이 무사히 잘 돌아가면 최댓값 확인 
    
    print(f'#{tc} {max_danjo}')