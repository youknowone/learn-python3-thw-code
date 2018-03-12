print("모든 것을 연습해 봅시다.")
print('\\를 이용해 \n 새줄이나 \t 탭을 하는 탈출순서열에 대해 \'알아야만\' 합니다.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print("이 값은 다섯입니다: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print(f"시작점: {}".format(start_point))
# it's just like with an f"" string
print(f"{beans}알, {jars}그릇, {crates}상자가 있습니다.")

start_point = start_point / 10

print("이렇게 할 수도 있습니다.")
# 리스트를 포맷 문자열에 적용하는 쉬운 방법이지요
print("젤리 {}개, {}그릇, {}상자가 있습니다.".format(*formula))