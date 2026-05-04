def sungjuk_process():
    prompt = '''
            *** 원하는 메뉴 번호를 선택하세요. ***
            1. 추가
            2. 삭제
            3. 출력
            4. 끝내기
        '''
    sungjuk_list = []

    while True:
        try: 
            choice = input(prompt)
            if choice == '1':
                sno = int(input('번호 : '))
                sname = input('이름 : ')
                score = int(input('점수 : '))
                sungjuk_list.append([sno, sname, score])
                print('새로운 학생정보가 추가되었습니다.')
            elif choice == '2':
                print('현재 저장된 아이템의 갯수는 {}개 입니다.'.format(len(sungjuk_list)))
                index = int(input('제거할 아이템의 순번 : '))
                if index < len(sungjuk_list):
                    sungjuk_list.pop(index)
                    print(index,'번 위치의 아이템이 제거되었습니다.')
                    print('현재 저장된 아이템의 갯수는 {}개 입니다.'.format(len(sungjuk_list)))
                else:
                    print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')
            elif choice == '3':
                for i in range(len(sungjuk_list)):
                    print(i, ':', sungjuk_list[i])
            elif choice == '4':
                print('성적관리 프로그램이 종료되었습니다.')
                break
            else:
                print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')
        except:
            print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.')