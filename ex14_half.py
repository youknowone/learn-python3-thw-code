### @export "setup"
import fake_input
input, input = fake_input.create(['Yes',
                                   "San Francisco",
                                   'Tandy 1000'])

### @export "code"
from sys import argv

script, user_name = argv
prompt = '> '

print(f"안녕 {user_name}, 나는 {script} 스크립트야.")
print("몇 가지 질문을 할게.")
print(f"{user_name}, 나를 좋아해?")
likes = input(prompt)

print(f"{user_name}, 어디에 살아?")
lives = input(prompt)

print("무슨 종류의 컴퓨터를 갖고 있어?")
computer = input(prompt)

print(f"""
좋아, 나를 좋아하냐는 질문에는 {likes}.
{lives}에 살아.  어딘지는 모르겠지만.
그리고 {computer} 컴퓨터를 가졌어.  근사한걸.
""")
