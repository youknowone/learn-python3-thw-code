
def 단어_쪼개기(값):
    """문자열을 단어 단위로 쪼개 줍니다"""
    단어들 = 값.split(' ')
    return 단어들

def 단어_정렬(단어들):
    """단어를 정렬합니다"""
    return sorted(단어들)

def 첫_단어_출력(단어들):
    """첫 단어를 꺼내고 출력합니다."""
    단어 = 단어들.pop(0)
    print(단어)

def 마지막_단어_출력(단어들):
   """마지막 단어를 꺼내고 출력합니다."""
   단어 = 단어들.pop(-1)
   print(단어)

def 문장_정렬(문장):
    """한 문장을 통째로 받아 정렬된 단어를 반환합니다."""
    단어들 = 단어_쪼개기(문장)
    return 단어_정렬(단어들)

def 처음과_마지막_단어_출력(문장):
    """문장의 처음과 마지막 단어를 출력합니다."""
    단어들 = 단어_쪼개기(문장)
    첫_단어_출력(단어들)
    마지막_단어_출력(단어들)

def 정렬_후_처음과_마지막_단어_출력(문장):
    """단어를 정렬하고 처음과 마지막 단어를 출력합니다."""
    단어들 = 문장_정렬(문장)
    첫_단어_출력(단어들)
    마지막_단어_출력(단어들)