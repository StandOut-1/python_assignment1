import os

def emp_process():
    prompt = '''
            *** 직원 정보 관리 서비스 ***
            1. 새 직원정보 추가
            2. 직원정보 삭제
            3. 전체 출력
            4. 파일에 저장
            5. 파일로 부터 직원정보 읽어오기
            9. 서비스 끝내기
            '''
    
    emp_dict = {}

    while True:
        try:
            choice = input(prompt)
            if choice == '1':
                empid = input('사번 : ')
                empname = input('이름 : ')
                empno = input('주민번호 : ')
                email = input('이메일 : ')
                phone = input('전화번호 : ')
                salary = int(input('급여 : '))
                job = input('직급 : ')
                dept = input('부서 : ')
                emp_dict[empid] = [empid, empname, empno, email, phone, salary, job, dept]
                print(empid, '번 사번의 직원 정보가 추가되었습니다.')
                print(emp_dict[empid])
            elif choice == '2':
                print('현재 저장된 아이템의 갯수는 {}개 입니다.'.format(len(emp_dict)))
                del_id = input('삭제할 사번 : ')
                if del_id in emp_dict:
                    del emp_dict[del_id]
                    print(del_id, '번 사번의 직원 정보가 삭제되었습니다.')
                    print('현재 저장된 아이템의 갯수는 {}개 입니다.'.format(len(emp_dict)))
                else:
                    print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')
            elif choice == '3':
                for i in emp_dict:
                    print(i, ':', emp_dict[i])
            elif choice == '4':
                filename = input('저장할 파일명 : ')
                f= open(filename, 'w')
                f.write(str(emp_dict))
                f.close()
                print('성공적으로 저장되었습니다.')
            elif choice == '5':
                filename = input('읽을 파일명 : ')
                f = open(filename, 'r')
                emp_dict = eval(f.read())
                print(emp_dict)
            elif choice == '9':
                print('서비스 끝내면서 프로그램 종료되게 함')
                break
            else:
                print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')
        except:
            print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')
                
