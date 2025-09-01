T = int(input())
# 테스트케이스
for tc in range(1, T+1):
    # 테스트케이스 반복
    arr = list(map(int, input().split()))
    # 숫자배열 인풋 리스트로 받아오기
    odd_sum = 0
    # 더할 값 초기화
    for i in arr:
        if i % 2 != 0:
            odd_sum += i
    # 배열 반복 돌면서 홀수면 더함

    print(f'#{tc} {odd_sum}')
    # 최종값 출력