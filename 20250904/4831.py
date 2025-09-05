T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # K = 한번 충전으로 이동하는 정류장 수, N = 총 정류장 수 M = 충전기가 설치된 정류장 수
    # 3 10 5면
    input_1 = list(map(int, input().split()))
    # 정류소 위치 리스트로 받아주고
    elec_bus_stop = [0] + input_1 + [N]
    # 연산이 쉽도록 출발지와 도착지를 추가로 리스트에 넣어줌

    fail = False
    # K값보다 각 거리가 먼 정류장이 있으면 애초에 집에못감
    for j in range(len(elec_bus_stop) - 1):
        if elec_bus_stop[j+1] - elec_bus_stop[j] > K:
            fail = True
            break

    if fail:
        # fail 이 true면
        print(f'#{tc} 0')
        # 0을 출력하고 다음 테케로
        continue

    charge_cnt = 0
    # 충전횟수 기록 변수
    i = 0
    # 버스의 진행상황 기록 변수(충전소가 있는 버정 인덱스)
   
    while i < len(elec_bus_stop) - 1:
    # 현재 위치(i)에서 K만큼 갔을 때, 갈 수 있는 가장 먼 충전소의 인덱스를 찾음
        farthest_stop_idx = i
        for j in range(i + 1, len(elec_bus_stop)):
            # 현재 위치에서 j번째 충전소까지의 거리가 K 이하인 경우
            if elec_bus_stop[j] - elec_bus_stop[i] <= K:
                # 갈 수 있는 곳이므로, 가장 먼 곳의 인덱스를 갱신
                farthest_stop_idx = j
            else:
                # K를 초과하면 더 이상 갈 수 없으므로 탐색 중단
                break

        # 가장 멀리 갈 수 있는 곳이 종점(N)이라면, 더 이상 충전할 필요 없음
        if farthest_stop_idx == len(elec_bus_stop) - 1:
            break
            
        # 반례 다 통과하면 가장 멀리 갈 수 있는 충전소로 이동하여 충전
        i = farthest_stop_idx
        charge_cnt += 1

    print(f'#{tc} {charge_cnt}')
