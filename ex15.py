### @export "setup"
import fake_input
input, input = fake_input.create(['ex15_sample.txt'])

### @export "code"
from sys import argv

스크립트, 파일_이름 = argv

텍스트 = open(파일_이름)

print(f"파일 {파일_이름}의 내용:")
print(텍스트.read())

print("파일이름을 다시 입력해 주세요.")
파일_한번더 = input("> ")

텍스트_한번더 = open(파일_한번더)

print(텍스트_한번더.read())
