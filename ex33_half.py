i = 0
numbers = []

while i < 6:
    print(f"꼭대기에서 i는 {i}")
    numbers.append(i)

    i = i + 1
    print("숫자는 이제: ", numbers)
    print(f"바닥에서 i는 {i}")


print("숫자: ")

for num in numbers:
    print(num)

