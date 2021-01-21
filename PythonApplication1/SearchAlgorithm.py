#[?] 정렬되어 있는 데이터를 이진 검색(이분 탐색)을 활용하여 반씩 나눠서 검색

# 검색 알고리즘: 주어진 데이터에서 특정 데이터를 찾는 프로그램
def main():
	#[0] Init(초기화):
	
	#[1] Input(입력): Data Structure(Array, List, Stack, Pop, Queue, Tree, DB, ...)
	data = [1, 3, 5, 7, 9, 10, 12, 14, 16, 18, 20, 21, 23, 25, 27, 29] # 오름차순으로 정렬되었다고 가정
	N = len(data)
	search = 18 # 검색할 데이터
	flag = False # 플래그 변수: 최종적으로 찾으려는 데이터를 찾으면 True 찾지 못하면 False를 저장시키는 변수
	index = -1 # 인덱스 변수: 찾은 위치, -1은 만족하는 데이터가 없다는 표현
	cnt = 0 # 탐색 횟수 카운팅

	#[2] Process(처리): Binary Search Algorithm
	low = 0
	high = N - 1
	while(low <= high):
		cnt += 1
		mid = (int) ((low + high) / 2)
		print(f'{cnt}번 작업 후 mid 값: {mid}, {mid}번째 데이터 값: {data[mid]}')
		if data[mid] == search:
			flag = True; index = mid; break; # 찾으면 플래그와 인덱스 저장 후 종료
		if data[mid] < search:
			low = mid + 1 # 찾을 데이터가 크면 오른쪽 영역으로 이동 후 이어서 진행
		else:
			high = mid - 1 # 찾을 데이터가 작으면 왼쪽 영역으로 이동 후 이어서 진행

	#[3] Output(출력): UI(Console, Desktop, Web, Mobile, ...)
	if flag:
		print(f'{cnt}번의 탐색 끝에 {search}을(를) data set의 {index}번째 위치에서 찾았습니다.')
	else:
		print("찾지 못하였습니다.")

if __name__ == "__main__":
	main()

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5