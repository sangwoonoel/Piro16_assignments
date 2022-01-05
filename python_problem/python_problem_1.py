class NotOneTwoThreeError(Exception):
      def __init__(self):
            super().__init__('1,2,3 중 하나를 입력하세요')
num = 0
game = 0 #게임 숫자를 저장하는 변수
turn = 0 #누구의 턴인지 저장하는 변수

while True:
      if game == 31:
            break
                        
      turn += 1
      while True:
            try:
              num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
              if num > 3 or num < 1:
                    raise NotOneTwoThreeError
            except ValueError:
              print('정수를 입력하세요')
            except NotOneTwoThreeError as e:
              print(e)
            else:
                  break

      if turn % 2 != 0:
            for i in range(num):
                  game += 1
                  if game == 31:
                        print('playerB win!')
                        break
                        
                  print('playerA : ', game)
      else:
            for i in range(num):
                  game += 1
                  if game == 31:
                      print('playerA win!')
                      break
                        
                  print('playerB : ', game)
    
          
                
            



