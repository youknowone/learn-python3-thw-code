# argv를 쓴 스크립트와 비슷한 함수
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# 좋아요. 사실 *args는 필요가 없습니다. 그냥 이렇게 하죠.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# 이 함수는 실행인자를 하나만 받습니다
def print_one(arg1):
    print(f"arg1: {arg1}")

# 이 함수는 실행인자를 하나도 받지 않습니다
def print_none():
    print("I got nothin'.")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

