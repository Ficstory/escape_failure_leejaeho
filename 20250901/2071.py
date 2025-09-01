T = int(input())
# 테스트케이스
for tc in range(1, T+1):
    # 테스트케이스 반복
    arr = list(map(int, input().split()))
    # 리스트로 숫자 배열 받아오기
    s = sum(arr)
    # 더하기
    ans = s / 10
    # 문제에서 10개로 정해놓았으므로 평균값 구하기위해 10개로 나누기
    answer = round(ans)
    # 반올림

    print(f'#{tc} {answer}')
    # 출력