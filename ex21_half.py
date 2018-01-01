
def add(a, b):
    print(f"덧셈 {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"뺄셈 {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"곱셈 {a} * {b}")
    return a * b

def divide(a, b):
    print(f"나눗셈 {a} / {b}")
    return a / b


print("함수만으로 계산해 봅시다!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"나이: {age}, 키: {height}, 몸무게: {weight}, IQ: {iq}")


# 추가 점수 문제. 아무렇게나 쓰세요.
print("문제를 하나 드릴게요.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("결과: ", what, "손으로 계산할 수 있나요?")
