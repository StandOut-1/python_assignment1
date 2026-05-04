import fileio.fileio_mission as fileio
import loop.while_mission as while_mission

def menu():
    prompt = '''
	*** 파이썬 과제 1 ***
	1. while 실습문제
	2. fileio 실습문제
	9. 과제 실행 테스트 끝내기
 '''
    
    while True:
        print(prompt)

        try:
            choice = input('선택하세요 : ')
            if choice == '1': # while 문 실습문제 요구사항 ---------------------------------------------------------
               while_mission.sungjuk_process()
            elif choice == '2': # fileio 실습문제 요구사항 ---------------------------------------------------------
              fileio.emp_process()
            elif choice == '9': # 과제 실행 테스트 끝내기
                break
            else:
                print('잘못 입력하였습니다. 확인하고 다시 입력하세요.')

        except KeyboardInterrupt:
            print('사용자의 요청에 의해 프로그램이 종료되었습니다.')
            break
        except Exception as e:
            print(f'에러 발생: {e}\n다시 입력하세요.')

if __name__ == '__main__':
    menu()