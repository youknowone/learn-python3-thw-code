ten_things = "사과 귤 까마귀 전화기 빛 설탕"

print("잠깐 아직 목록에 10개가 들어있지 않으니 한 번 고쳐 봅시다.")

stuff = ten_things.split(' ')
more_stuff = ["낮", "밤", "노래", "부메랑",
              "옥수수", "바나나", "아이", "어른"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("추가: ", next_one)
    stuff.append(next_one)
    print(f"이제 {len(stuff)} 항목이 있습니다.")

print("한 번 볼까요! ", stuff)

print("이걸로 무언가 해 봅시다.")

print(stuff[1])
print(stuff[-1]) # 워어! 좋은데?
print(stuff.pop())
print(' '.join(stuff)) # 뭐? 멋져!
print('#'.join(stuff[3:5])) # 엄청나구나!
