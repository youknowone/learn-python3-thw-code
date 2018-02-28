
the_count = [1, 2, 3, 4, 5]
fruits = ['사과', '귤', '배', '살구']
change = [1, '십원', 2, '백원', 3, '오백원']

# 첫 번째 for 순환문은 list를 따라 돕니다
for number in the_count:
    print(f"이 수는 {number}")

# 위와 같아요
for fruit in fruits:
    print(f"과일 중류: {fruit}")

# 섞어 만든 list도 돌 수 있어요
for i in change:
    print(f"받은 잔돈 {i}")

# list를 만들 수도 있는데, 먼저 빈 것으로 시작합시다
elements = []

# 그리고 0에서 5까지 세는 range 함수를 써요
for i in range(0, 6):
    print(f"list에 {i} 숫자를 더합니다.")
    # append는 list가 알아듣는 함수입니다
    elements.append(i)

# 이것도 출력할 수 있습니다
for i in elements:
    print(f"원소는 {i}")

