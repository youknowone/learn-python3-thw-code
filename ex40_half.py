
class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["생일 축하 합니다",
                   "고소당하기는 싫으니까",
                   "여기서 이만 할게요"])

bulls_on_parade = Song(["조개 껍질 한가득 차고",
                        "가장을 위한다지"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
