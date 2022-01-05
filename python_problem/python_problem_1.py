class NotOneTwoThreeError(Exception):
     def __init__(self):
         super().__init__('1,2,3 중 하나를 입력하세요')

num = 0
game = 0 #게임 숫자를 세주는 변수


while True:
 while True:
  try:
   num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
   if num > 3 or num < 1:
    raise NotOneTwoThreeError
  except ValueError:
   print('정수를 입력하세요')
  except NotOneTwoThreeError as e:
   print(e)
  else:
   break

 for i in range(num):
  game += 1
  print('PlayerA :', game)
