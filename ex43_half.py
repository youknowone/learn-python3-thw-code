### @export "fake"
import fake_input
input, input = fake_input.create(['회피!'])

### @export "imports"

from sys import exit
from random import randint
from textwrap import dedent

### @export "scene_class"

class Scene(object):

    def enter(self):
        print("아직 만들지 않은 장면입니다.")
        print("상속해 enter()를 구현하세요.")
        exit(1)

### @export "engine_class"

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

### @export "death_scene"

class Death(Scene):

    quips = [
        "사망. 진짜 못하네요.",
        "어머니가 자랑스러워 하시겠어요... 좀 더 똑똑하셨다면요.",
        "패배자 같으니.",
        "내가 기르는 강아지도 이거보단 잘 해요.",
        "부장님이 개그를 해도 이거보단 잘하겠네요."

    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


### @export "center_corridor"

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
              페르칼 25번 행성의 고던족은 여러분의 우주선에 침략하고 모든
              승무원을 죽였습니다. 당신은 마지막 생존자이며 마지막 임무로
              무기고에서 중성자파괴탄을 가져와 함교에 설치하고 구명정에 타기
              전에 우주선을 폭파해야합니다.

              붉은 비늘 피부, 시커먼 때가 낀 이빨, 증오로 가득 찬 몸에서 물
              흐르듯 이어지는 사악한 광대 복장의 고던인이 뛰쳐 나오는 동안
              당신은 중앙 복도에서 무기고로 내달리고 있습니다. 고던인은
              무기고로 가는 문을 가로막고 당신을 날려버리러 무기를 겨누는
              참입니다.
              """))

        action = input("> ")

        if action == "발사!":
            print(dedent("""
                  당신은 광선총을 빼들기가 무섭게 고던인을 쏘아버립니다.
                  고던인의 광대 옷이 휘날려 몸을 숨겨주고 당신의 조준을
                  흩뜨립니다. 광선은 옷은 맞추었지만 고던인은 완전히
                  놓쳐버립니다. 어머니가 사 준 신상 옷을 모조리 망쳐버리자
                  고던인은 광기 어린 분노에 빠져들어 당신이 죽을 때까지
                  얼굴을 쏘아댑니다. 고던인은 당신을 먹어치웁니다.
                  """))
            return 'death'

        elif action == "회피!":
            print(dedent("""
                  국제경기급 권투 선수처럼 달리고 피하고 구르고 오른쪽으로
                  미끄러져 고던인의 광선총이 당신의 머리 옆을 빗겨 쏘도록
                  합니다. 예술적인 회피를 하는 와중 그만 발이 미끄러져 금속
                  벽에 머리를 찧고 기절합니다. 잠시 후 정신을 차리지만
                  고던인은 그저 머리를 짓밟아 죽이고는 잡아 먹을 뿐입니다.
                  """))
            return 'death'

        elif action == "농담하기":
            print(dedent("""
                  운좋게도 당신은 학교에서 고던어 욕설을 배웠습니다. 아는
                  고던 농담을 하나 합니다.
                  Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                  fur fvgf nebhaq gur ubhfr.
                  고던인은 멈춰서서 웃지 않으려 애쓰지만, 결국 웃음보가
                  터지자 꼼짝도 하지 못합니다. 당신은 고던인이 웃어대는
                  틈에 뛰쳐나가 정통으로 머리를 맞춰 쓰러뜨리고 무기고의
                  문으로 뛰어듭니다.
                  """))
            return 'laser_weapon_armory'

        else:
            print("처리할 수 없습니다!")
            return 'central_corridor'

### @export "game_scenes"

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
              당신은 무기고로 뛰어 들어 구르고는 쪼그려 앉야 혹시
              숨어있을지도 모르는 고던인을 찾아 방을 살핍니다. 쥐 죽은
              듯이, 지나칠 만큼 조용합니다. 일어서서는 문 건너편으로
              달려 보관함에서 중성자파괴탄을 찾습니다. 보관함은
              비밀번호로 잠겨 있고 중성자파괴탄을 꺼내려면 비밀번호를
              알아내야만 합니다. 비밀번호를 10번 틀리면 자물쇠는
              영원히 잠기고 폭탄은 꺼낼 수 없습니다. 비밀번호는 3자리
              수입니다.
              """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[번호판]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("삐비비빅!")
            guesses += 1
            guess = input("[번호판]> ")

        if guess == code:
            print(dedent("""
                  보관함이 철컥하며 열리며 밀폐가 풀리자 공기가
                  새어나옵니다. 중성자파괴탄을 움켜쥐고 설치해야 할 장소인
                  함교를 향해 할 수 있는 한 가장 빠른 속도로 내달립니다.
                  """))
            return 'the_bridge'
        else:
            print(dedent("""
                  마지막 기회가 지나자 자물쇠가 웅웅거리며 기계장치가
                  엉겨 붇으며 녹아내리는 소름끼치는 소리가 들립니다.
                  당신은 거기 주저앉아 있기로 마음먹었고, 결국 고던
                  우주선이 당신네 우주선을 터뜨려 죽음을 맞습니다.
                  """))
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print(dedent("""
              겨드랑이에 중성자파괴탄을 끼고 함교로 뛰어들어 우주선
              조종권을 탈취하던 고던인 5명을 놀래킵니다. 그 모두가
              아까 본 고던인보다도 더 흉측한 광대 복장을 하고
              있습니다. 고던인들은 아직 무기를 뽑지는 않았는데,
              활성화된 폭탄을 든 걸 보자 더욱이 터뜨리지 않고
              싶어합니다.
              """))

        action = input("> ")

        if action == "폭탄 던지기":
            print(dedent("""
                  당신은 당황해서는 고던인 무리에 폭탄을 집어 던지고는
                  문으로 펄쩍 뛰어 오릅니다. 폭탄을 놓자마자 고던인
                  하나가 등 뒤를 정확히 쏴 맞춰 죽여버립니다.
                  당신은 죽어가는 동안 다른 고던인이 미친듯이 폭탄을
                  해체하려 달려드는 것을 봅니다. 죽음을 맞는 동안
                  폭탄이 터지면 고던인 모두가 터져 나가리라고
                  생각합니다.
                  """))
            return 'death'

        elif action == "천천히 폭탄 설치하기":
            print(dedent("""
                  폭탄을 광선총으로 겨누자 고던인들은 두 손을 들고
                  삐질삐질 땀을 흘리기 시작합니다. 당신은 문 뒤에
                  바짝 붙어서는, 문을 열고, 광선총을 그대로 겨눈 채로,
                  조심스레 폭탄을 바닥에 설치합니다. 곧 이어 문 밖으로
                  뛰쳐나와 닫기 단추를 두들기고는 잠금장치를 쏴 갈겨
                  고던인들이 빠져 나올 수 없도록 만들어버립니다.
                  이제 폭탄은 설치되었고, 이 깡통에서 벗어나도록
                  구명정으로 내달립니다.
                  """))

            return 'escape_pod'
        else:
            print("처리할 수 없습니다!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
              우주선이 통째로 폭발하기 전에 구명정에 닿기 위해
              우주선을 가로질러 필사적으로 달립니다. 우주선에는
              고던인이 거의 없어 방해받지 않고 질주합니다. 구명정이
              있는 방에 도달한 당신은 어떤 걸 탈지 하나를 골라야
              합니다. 이 가운데 몇 개는 손상되었을 수도 있지만 살펴볼
              시간이 없습니다. 구명정은 5대가 있습니다. 몇 번을
              타겠습니까?
              """))

        good_pod = randint(1, 5)
        guess = input("[구명정 번호]> ")


        if int(guess) != good_pod:
            print(dedent(f"""
                  {guess}번 구명정으로 뛰어들어 탈출 단추를 누릅니다.
                  구명정이 우주의 진공으로 나아가자마자, 선체가
                  파열해 찌그러져 들며 당신을 곤약처럼 으스러뜨립니다.
                  """))
            return 'death'
        else:
            print(dedent(f"""
                  {guess}번 구명정으로 뛰어들어 탈출 단추를 누릅니다.
                  구명정은 가볍게 우주로 미끄러져 나가며 아래의
                  행성으로 향합니다. 행성으로 향하는 동안 뒤를 돌아보자
                  당신네 우주선이 붕괴했다가는 밝은 별처럼 폭발하며 고던
                  우주선까지 휩쓸어 버리는 것을 확인합니다. 승리!
                  """))

            return 'finished'


class Finished(Scene):

    def enter(self):
        print("승리했습니다! 잘 했어요.")
        return 'finished'


### @export "map_class"

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

### @export "final_run"

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()