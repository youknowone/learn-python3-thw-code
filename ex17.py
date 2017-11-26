### @export "fake"
import fake_input
input, input = fake_input.create([''])

### @export "code"
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"{from_file} 에서 {to_file} 로 복사합니다")

# 이 두 줄은 한 줄로도 쓸 수 있습니다. 어떻게 할까요?
in_file = open(from_file)
indata = in_file.read()

print(f"입력 파일은 {len(indata)}바이트입니다")

print(f"출력 파일이 존재하나요? {exists(to_file)}")
print("준비되었습니다. 계속하려면 리턴을, 취소하려면 CTRL-C를 누르세요.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("좋습니다. 모두 완료되었습니다.")

out_file.close()
in_file.close()
