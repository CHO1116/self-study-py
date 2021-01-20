#[?] 주어진 데이터 중 가장 큰 값 구하기
import sys

# 최댓값 알고리즘: 주어진 범위에 주어진 조건에 해당하는 자료들 중 가장 큰 값

def main():
    #[0] Init(초기화):
    max = -sys.maxsize - 1 # 숫자 형식의 데이터 중 가장 작은 값으로 초기화
    
    #[1] Input(입력):
    numbers = [-2, -5, -7, -1, -15]; # MAX: -1
    N = len(numbers)

    #[2] Process(처리): 주어진 범위에 주어진 조건 (필터링)
    for i in range(0, N): # 주어진 범위
        if max < numbers[i]: # 더 큰 데이터가 있다면
            max = numbers[i] # MAX 값 할당

    #[3] Output(출력):
    print(f'주어진 자료값 중 최댓값: {max}')

if __name__ == "__main__":
    main()

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5
