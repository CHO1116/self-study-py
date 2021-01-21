#[?] 무작위 데이터를 순서대로 [오름차순(ASC)/내림차순(DESC)] 정렬
import sys

# 정렬 알고리즘: 가장 [작은/큰] 데이터를 왼쪽으로 순서대로 이동

def main():
    #[0] Init(초기화):
    
    #[1] Input(입력): Data Structure(Array, List, Stack, Pop, Queue, Tree, DB, ...)
    data = [ 3, 2, 1, 5, 4 ] # 정렬되지 않은 data
    N = len(data)
    print(f' 초기 데이터 셋: {data}')

    #[2] Process(처리): Selection Sort Algorithm
    for i in range(0, N - 1): # i = 0 to N - 1
        print(f'{i + 1}번째 sort 과정:')
        for j in range(i + 1, N): # j = i + 1 to N
            if data[i] > data[j]: # 오름차순인 경우/내림차순은 반대로 부등호 설정
                temp = data[i]; data[i] = data[j]; data[j] = temp # SWAP
            print(data)
        print(f'{i + 1}번째 sort 결과: {data}')

    #[3] Output(출력): UI(Console, Desktop, Web, Mobile, ...)
    for i in range(N):
        print(data[i])

if __name__ == "__main__":
    main()

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5