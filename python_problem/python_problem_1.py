from random import randint

class NotOneTwoThreeError(Exception):
      def __init__(self):
            super().__init__('1,2,3 중 하나를 입력하세요')
num = 0
game = 0 #게임 숫자를 저장하는 변수
turn = 0 #누구의 턴인지 저장하는 변수

def brgame():
      if turn % 2 != 0: 
            num = randint(1,3)
      else:
            num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : "))
            if num > 3 or num < 1:
                  raise NotOneTwoThreeError
      for i in range(num):
            global game
            game += 1            
                        
            if turn % 2 != 0:             
                  print('computer : ', game)
                  if game == 31:
                        print('player win!')
                        return 0 

            else:
                  print('player : ', game)
                  if game == 31:
                        print('computer win!')
                        return 0

while True:                    
      turn += 1
      while True:
            try:
                  end = brgame()
            except ValueError:
              print('정수를 입력하세요')
            except NotOneTwoThreeError as e:
              print(e)
            else:
                  break

      
      if end == 0:
            break

    
          
                
            



