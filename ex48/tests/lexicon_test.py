from ex48 import lexicon


def test_directions():
    assert lexicon.스캔("북") == [('방향', '북')]
    결과 = lexicon.스캔("북 남 동")
    assert 결과 == [('방향', '북'),
                    ('방향', '남'),
                    ('방향', '동')]

def test_verbs():
    assert lexicon.스캔("이동") == [('동사', '이동')]
    결과 = lexicon.스캔("이동 공격 섭취")
    assert 결과 == [('동사', '이동'),
                    ('동사', '공격'),
                    ('동사', '섭취')]


def test_stops():
    assert lexicon.스캔("그") == [('제외', '그')]
    결과 = lexicon.스캔("이 그 저")
    assert 결과 == [('제외', '이'),
                    ('제외', '그'),
                    ('제외', '저')]


def test_nouns():
    assert lexicon.스캔("곰") == [('명사', '곰')]
    결과 = lexicon.스캔("곰 공주")
    assert 결과 == [('명사', '곰'),
                    ('명사', '공주')]

def test_numbers():
    assert lexicon.스캔("1234") == [('숫자', 1234)]
    결과 = lexicon.스캔("3 91234")
    assert 결과 == [('숫자', 3),
                    ('숫자', 91234)]


def test_errors():
    assert lexicon.스캔("ㅁㄴㅇㄹ") == [('오류', 'ㅁㄴㅇㄹ')]
    결과 = lexicon.스캔("곰 공주 멁다")
    assert 결과 == [('명사', '곰'),
                    ('명사', '공주'),
                    ('오류', '멁다')]