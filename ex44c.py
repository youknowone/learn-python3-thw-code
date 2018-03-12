class 부모(object):

    def 대체하기(self):
        print("부모 대체하기()")

class 자식(부모):

    def 대체하기(self):
        print("자식, 부모 대체하기() 이전")
        super(자식, self).대체하기()
        print("자식, 부모 대체하기() 이후")

아빠 = 부모()
아들 = 자식()

아빠.대체하기()
아들.대체하기()
