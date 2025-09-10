
def merge(left, right):
    # 병합을 위한 함수, 왼쪽 리스트, 오른쪽 리스트를 각각 받아옴
    result = [0] * (len(left) + len(right))
    # 결과를 저장할 리스트
    l = r = 0
    # 비교하기 위한 리스트 인덱스 변수 설정

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    while l < len(left) and r < len(right):
        # 왼쪽 길이가 왼쪽 인덱스 보다 크고, 오른쪽 길이가 오른쪽 인덱스 보다 큰 경우에만 반복
        if left[l] > right[r]:
            # 왼쪽이 더 큰 경우
            result[l + r] = right[r]
            # 왼쪽 인덱스와 오른쪽 인덱스를 더한 곳에 작은 값을 넣어주고
            r += 1
            # 오른쪽 인덱스 하나 더해줌
            
            
        else:
            result[l + r] = left[l]
            # 오른쪽이 큰 경우와 같은경우 
            # 작거나 같은 값을 왼쪽에 넣어줌
            l += 1
            # 왼쪽 인덱스를 더해줌
            

    # 왼쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result

    
def merge_list(slice_list):
    # 종료조건
    # 더이상 나눌 수 없을때 : 길이가 1일때
    if len(slice_list) == 1:
        return slice_list
    mid = len(slice_list) // 2
    # 중간값 기준으로 슬라이스 하기위해 중간값을 구해줌
    left_slice = slice_list[:mid]
    right_slice = slice_list[mid:]
    
    # 슬라이스 된 리스트를 다시 함수에 넣어가지고 더 쪼개줌
    # 왼쪽 오른쪽 두번을 재귀해야함
  
    left_list = merge_list(left_slice)
    right_list = merge_list(right_slice)

    global cnt
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 세기위한 전역변수 설정
    if left_list[-1] > right_list[-1]:
        cnt += 1
    # 왼쪽이 큰경우를 세야해서 카운트 1
    
    merged_list = merge(left_list, right_list)
    # 그리고 병합과정을 함수로 따로 만들어줌
    return merged_list
    
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 정렬할 배열을 받아온다
    # 병합정렬을 하려면 일단 정렬하는 함수를 정의, 그리고 합치는 함수를 정의해야함
    # 문제에서 병합과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 세야함
    cnt = 0
    # 세기위한 전역변수 설정
    sorted_arr = merge_list(arr)
    # 정렬을 위한 함수 설정
    mid = N // 2
    # 중간값 출력을 위해 중간 인덱스 구하고
    answer = sorted_arr[mid] 
    # 중간값 구하기
    print(f'#{tc} {answer} {cnt}')

    


    
    
    


