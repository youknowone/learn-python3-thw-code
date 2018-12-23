### @export "setup"
import fake_input
input, input = fake_input.create(['ex15_sample.txt'])

### @export "code"
from sys import argv

script, filename = argv

txt = open(filename, encoding='utf-8')

print(f"파일 {filename}의 내용:")
print(txt.read())

print("파일이름을 다시 입력해 주세요.")
file_again = input("> ")

txt_again = open(file_again, encoding='utf-8')

print(txt_again.read())
