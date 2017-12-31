### @export "setup"
echo "1번 줄입니다" > test.txt
echo "2번 줄입니다" >> test.txt
echo "3번 줄입니다" >> test.txt
### @export "run"
python3.6 ex20.py test.txt
