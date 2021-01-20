#[?] 주어진 데이터 중 가장 작은 [짝수] 값 구하기
import sys

# 최솟값 알고리즘: 주어진 범위에 주어진 조건에 해당하는 자료들 중 가장 작은 값

def main():
    #[0] Init(초기화):
    min = sys.maxsize # 숫자 형식의 데이터 중 가장 큰 값으로 초기화
    
    #[1] Input(입력):
    numbers = [-2, -5, -7, -1, -15] # MIN: -15
    N = len(numbers)

    #[2] Process(처리): 주어진 범위에 주어진 조건 (필터링)
    for i in range(0, N): # 주어진 범위
        if min > numbers[i] and numbers[i] % 2 == 0: # 짝수이면서 더 작은 데이터가 있다면
            min = numbers[i] # MIN 값 할당

    #[3] Output(출력):
    print(f'주어진 자료값 중 짝수 최솟값: {min}')

if __name__ == "__main__":
    main()

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5