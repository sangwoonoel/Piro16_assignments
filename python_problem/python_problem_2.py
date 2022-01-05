#1
class ExistError(Exception):
    pass
#2
class NoStudentError(Exception):
    pass
#3
class NoGradeError(Exception):
    pass
#4
class NotExistError(Exception):
    pass


exam_list = []

def Menu1(name, mid_score, final_score) :
    exam_list.append([name, mid_score,final_score])
    return

    #사전에 학생 정보 저장하는 코딩 
##############  menu 2
def Menu2() :
    for i in exam_list:
        averge = (i[1] + i[2]) / 2

        if averge >= 90:
            grade = 'A'
        elif averge >= 80:
            grade = 'B'
        elif averge >= 70:
            grade = 'C'
        else:
            grade = 'D'

        i.append(grade)
    return

##############  menu 3
def Menu3() :
    print('--------------------')
    print('name mid final grade')
    for i in exam_list:
        for j in i:
            print(j, end='  ')
        print()
    print('--------------------')

    #출력 코딩
def Menu4():
    j = 0
    for i in exam_list:
        if i[0] == del_name:
            del exam_list[j]
            print('{0} student information is deleted.'.format(del_name))
            j += 1


        

        #학생 정보 삭제하는 코딩
        



while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1" :
        try:
            name, mid_score, final_score  = input("Enter name mid-score final-score :").split()
            try:
                mid_score = int(mid_score)
                final_score = int(final_score)
            except ValueError:
                print("Score is not positive integer")
            if len(exam_list) != 0:
                for i in range(len(exam_list)):
                    if name == exam_list[i][0]:
                        raise ExistError('Already exist name!')

        except ValueError:
            print("Num of data is not 3!")
        except ExistError as e:
            print(e)
       
        else:
            Menu1(name, mid_score, final_score)
       


        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 

    elif choice == "2" :
        try: 
            if len(exam_list) == 0: # or len(exam_list) == len(grade_list):
                raise NoStudentError('No student data!')
        except NoStudentError as e:
            print(e)
        else:
            Menu2()
            print("Grading to all students.")
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    elif choice == "3" :
        try: 
            if len(exam_list) == 0: 
                raise NoStudentError('No student data!')
            for i in exam_list:
                if len(i) != 4:
                    raise NoGradeError("There is a student who didn't get grade.")
            
        except NoStudentError as e:
            print(e)

        except NoGradeError as e:
            print(e)
        else:
            Menu3()
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :
        try: 
            j = 0
            if len(exam_list) == 0: 
                raise NoStudentError('No student data!')
            del_name = input("Enter the name to delete : ")
            for i in exam_list:
                if i[0] == del_name:
                    j += 1
            if j == 0:
                raise NotExistError("Not exist name!")
                    
        except NoStudentError as e:
            print(e)
        except NotExistError as e:
            print(e)
        else:
            #else 부분 신경 쓰기
            Menu4()

        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        print("EXit Program!")
        break
        #프로그램 종료 메세지 출력
        #반복문 종료

    else :
        print("Wrong number. Choose again.")
        #"Wrong number. Choose again." 출력