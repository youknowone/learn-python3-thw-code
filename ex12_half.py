### @export "fake"
import fake_input
input, input = fake_input.create(['38', '6\'2"', '180lbs'])

### @export "code"
age = input("몇 살이죠? ")
height = input("키는 얼마죠? ")
weight = input("몸무게는 얼마죠? ")

print(f"네, 나이는 {age}살, 키는 {height}, 몸무게는 {weight}이네요.")

# see if this is nessessary
#print "뜬금없지만, 태양의 각지름은 %r입니다." % '''32'10"'''