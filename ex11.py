### @export "fake"
import fake_input
input, input = fake_input.create(['38', '6\'2"', '180lbs'])

### @export "code"
print("몇 살이죠?", end=' ')
age = input()
print("키는 얼마죠?", end=' ')
height = input()
print("몸무게는 얼마죠?", end=' ')
weight = input()

print(f"네, 나이는 {age}살, 키는 {height}, 몸무게는 {weight}이네요.")

# see this is nessessary or not
# print "뜬금없지만, 태양의 각지름은 %r입니다." % '''32'10"'''