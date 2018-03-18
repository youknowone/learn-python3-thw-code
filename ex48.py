# -*- coding: utf-8 -*-

from nose.tools import *
from ex47 import lexicon


def test_directions():
    assert_equal(lexicon.scan("북"), [('방향', '북')])
    result = lexicon.scan("북 남 동")
    assert_equal(result, [('방향', '북'),
                          ('방향', '남'),
                          ('방향', '동')])

def test_verbs():
    assert_equal(lexicon.scan("이동"), [('동사', '이동')])
    result = lexicon.scan("이동 공격 섭취")
    assert_equal(result, [('동사', '이동'),
                          ('동사', '공격'),
                          ('동사', '섭취')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])


def test_nouns():
    assert_equal(lexicon.scan("곰"), [('명사', '곰')])
    result = lexicon.scan("곰 공주")
    assert_equal(result, [('명사', '곰'),
                          ('명사', '공주')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('숫자', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('숫자', 3),
                          ('숫자', 91234)])


def test_errors():
    assert_equal(lexicon.scan("ㅁㄴㅇㄹ"), [('오류', 'ㅁㄴㅇㄹ')])
    result = lexicon.scan("곰 공주 멁다")
    assert_equal(result, [('명사', '곰'),
                          ('명사', '공주'),
                          ('오류', '멁다')])