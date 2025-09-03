T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # N을 받아옴
    arr = ""
    # 숫자를 저장할 배열

    i = 0
    # 한번두번 셀때마다 늘어나는 i
    while len(arr) < 10:
        # 10개가 되면 스탑
        i += 1
        K = N * i
        char = str(K)
        # 문자열로 바꾸고
        for c in char:
            # 순회해서
            if c not in arr:
                # 같은거 없으면 추가 
                arr += c

    print(f'#{tc} {K}')


