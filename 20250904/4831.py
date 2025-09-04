



T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # K = 한번 충전으로 이동하는 정류장 수, N = 총 정류장 수 M = 충전기가 설치된 정류장 수
    # 3 10 5면
    input_1 = list(map(int, input().split()))
    # 정류소 위치 리스트로 받아주고
    elec_bus_stop = [0] + input_1 + [N]
    # 연산이 쉽도록 출발지와 도착지를 추가로 리스트에 넣어줌

    charge_cnt = 0
    # 충전횟수 기록 변수
    i = 0
    # 버스의 진행상황 기록 변수
    remain = K
    # 충전없이 갈 수 있는 남은 거리

    while True:
        # 충전소 있는 마지막 정류장에 도착할때까지 반복
        i += 1
        # 일단 갑니다.
        remain = remain - (elec_bus_stop[i]-elec_bus_stop[i-1])
        # 가고나서 남은 연료 체크
        if i == M:
            # 만약에 마지막 충전소에 도착했으면
            if remain >= N - elec_bus_stop[M-1]:
                # 남은 거리가 종점까지까지 가는것보다 가까우면 충전없이 ㄱ
                break
            elif remain < N - elec_bus_stop[M-1]:
                # 남은 거리가 종점까지 가는것 보다 짧으면 충전하고 ㄱ
                charge_cnt += 1
                if K < N - elec_bus_stop[M-1]:
                    charge_cnt = 0
                break
        elif elec_bus_stop[i+1]-elec_bus_stop[i] > K:
            # 다음 충전소 까지 거리가 한번 충전해서 가는 거 보다 길면
            # 집에 못간다..
            charge_cnt = 0
            break
        else:
            # n번째 충전소에 도달
            # 만약에 다음 정류장까지 거리가 갈수 있는 거리와 같거나 짧으면
            if remain < elec_bus_stop[i+1] - elec_bus_stop[i]:
            # 만약에 다음 정류장까지 거리가 갈수 있는 거리보다 멀면
                charge_cnt += 1
                remain = K
                if remain < 0:
                    i -= 1

    print(f'#{tc} {charge_cnt}')
                    

