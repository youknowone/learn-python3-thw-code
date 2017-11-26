formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("하나", "둘", "셋", "넷"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "난 이게 있죠.",
    "지금 막 써 주신 그것.",
    "하지만 '노래'하진 않아요.",
    "그러니까 잘 자요."
))


# let's see issue #4
'''
formatter2 = "%r %r %r %r"
print formatter2 % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
'''