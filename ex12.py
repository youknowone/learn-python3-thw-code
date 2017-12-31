### @export "fake"
import fake_input
input, input = fake_input.create(['38', '188cm', '82kg'])

### @export "code"
나이 = input("몇 살이죠? ")
키 = input("키는 얼마죠? ")
몸무게 = input("몸무게는 얼마죠? ")

print(f"네, 나이는 {나이}살, 키는 {키}, 몸무게는 {몸무게}이네요.")

# see if this is nessessary
#print "뜬금없지만, 태양의 각지름은 %r입니다." % '''32'10"'''