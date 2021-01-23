#[?] 2개의 정수 배열 합치기

# 병합 알고리즘: 두 개의 정수 배열을 (응용: 각각 오름차순으로 정렬 후) 하나로 병합

def main():
	#[0] Init(초기화):
	
	#[1] Input(입력):
	first = [1, 4, 25, 8, 12, 5] # (응용) 오름차순 정렬, 갯수: 6
	second = [12, 6, 7, 10, 14, 22, 26, 9, 3] # (응용) 오름차순 정렬, 갯수: 9
	M = len(first)
	N = len(second)
	merge = [0] * (M + N) # 병합시키는 배열 표현
	i = 0; j = 0; k = 0

	#[2] Process(처리): 주어진 범위에 주어진 조건 (필터링)
	for x in range(0, M - 1): # 첫 번째 배열 오름차순 진행
		for y in range(x + 1, M):
			if (first[x] > first[y]):
				temp = first[x]; first[x] = first[y]; first[y] = temp

	for a in range(0, N - 1): # 두 번째 배열 오름차순 진행
		for b in range(a + 1, N):
			if (second[a] > second[b]):
				temp = second[a]; second[a] = second[b]; second[b] = temp

	while (i < M and j < N): # 둘 중 하나라도 배열의 끝에 도달할 때까지
		if first[i] < second[j]:
			merge[k] = first[i]
			k += 1; i += 1
		else:
			merge[k] = second[j]
			k += 1; j += 1

	while (i < M): # 첫 번째 배열이 끝까지 도달할 때까지
		merge[k] = first[i]
		k += 1; i += 1

	while (j < N): # 두 번째 배열이 끝까지 도달할 때까지
		merge[k] = second[j]
		k += 1; j += 1
	
	#[3] Output(출력):
	for item in merge:
		print(item, end = ' ')
	print()

if __name__ == "__main__":
	main()

#[!] 디버거 사용하기: F9 -> F5-> F11 -> F5