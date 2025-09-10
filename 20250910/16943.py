T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    list_A = sorted(A)
    list_B = list(map(int,input().split()))
    # N = A 리스트의 길이, A는 정렬된 상태로 저장해야함
    # M = B 리스트의 길이, B에 저장된 M개의 정수들이 A에 들어 있는지?

    # 찾아야하는것은 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽 구간을 번갈아 선택하게 되는 숫자의 개수
    # B에 있는 수가 A에 들어있으면서 중간값은 아니어야함
    cnt = 0
    
    for i in range(M):
        # B의 인덱스로 반복
        start = 0
        # 시작인덱스 초기 0
        end = N-1
        # 마지막인덱스 초기 N-1
        left_right_test = 0
        # 왼쪽 오른쪽 번갈아서
        find = False
        # 못찾으면 
        while start <= end:
            # 길이가 1개 이하면 종료
            mid = (start+end) // 2
            # 중간값 구해주기
            if list_A[mid] == list_B[i]:
                find = True
                # 만약에 중간값이 찾는 값이면 찾았다 TRUE로 바꾸고 종료
                break
            elif list_A[mid] > list_B[i]:
                # 만약에 중간값보다 찾는 값이 작을때
                if left_right_test == -1:
                    find = False
                    # 연속으로 왼쪽으로 가는지 확인
                    # 연속으로 가면 종료
                    break
                else :
                    # 번갈아 가는거 확인하면
                    end = mid - 1
                    # 마지막인덱스를 중간값 -1로 설정해주고 
                    left_right_test = -1
                    # 방향 바꿔줌
            else:
                # 만약에 중간값보다 찾는 값이 클때
                if left_right_test == 1:
                    # 연속으로 오른쪽으로 가는지 확인
                    # 연속으로 가면 종료
                    find = False
                    break
                else:
                    # 번갈아 가는거 확인하면
                    start = mid + 1
                    # 마지막인덱스를 중간값 -1로 설정해주고
                    left_right_test = 1
                    # 방향 바꿔줌
        if find == True :
            # 값도 찾았고 번갈아 가는지도 확인했으면 
            cnt +=1 
            # 카운트 1

    print(f'#{tc} {cnt}')




