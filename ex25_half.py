
def break_words(stuff):
    """문자열을 단어 단위로 쪼개 줍니다"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """단어를 정렬합니다"""
    return sorted(words)

def print_first_word(words):
    """첫 단어를 꺼내고 출력합니다."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
   """마지막 단어를 꺼내고 출력합니다."""
   word = words.pop(-1)
   print(word)

def sort_sentence(sentence):
    """한 문장을 통째로 받아 정렬된 단어를 반환합니다."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """문장의 처음과 마지막 단어를 출력합니다."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """단어를 정렬하고 처음과 마지막 단어를 출력합니다."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)