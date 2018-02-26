import sys
스크립트, input_encoding, error = sys.argv


def main(언어_파일, encoding, errors):
    줄 = 언어_파일.readline()

    if 줄:
        줄_출력(줄, encoding, errors)
        return main(언어_파일, encoding, errors)


def 줄_출력(줄, encoding, errors):
    next_lang = 줄.strip()
    원본_바이트열 = next_lang.encode(encoding, errors=errors)
    변환한_문자열 = 원본_바이트열.decode(encoding, errors=errors)

    print(원본_바이트열, "<===>", 변환한_문자열)


언어들 = open("languages.txt", encoding="utf-8")

main(언어들, input_encoding, error)

