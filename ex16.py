### @export "setup"
import fake_input
input, input = fake_input.create(['', 'Mary had a little lamb',
                                   'Its fleece was white as snow',
                                   'It was also tasty'])

### @export "code"
from sys import argv

script, filename = argv

print(f"{filename} 파일을 지우려 합니다.")
print("취소하려면 CTRL-C (^C) 를 누르세요.")
print("진행하려면 리턴 키를 누르세요.")

input("?")

print("파일 여는 중...")
target = open(filename, 'w')

print("파일 내용을 지웁니다.  안녕히!")
target.truncate()

print("이제 세 줄에 들어갈 내용을 부탁드릴게요.")

line1 = input("1줄: ")
line2 = input("2줄: ")
line3 = input("3줄: ")

print("이 내용을 파일에 씁니다.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("마지막으로 닫습니다.")
target.close()
