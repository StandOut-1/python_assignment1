# 🐍 파이썬 과제 1 (python_assignment1)

SK Playdata 과정 5월 4일 파이썬 기초 과제 수행 저장소입니다.

DAY04 상세기록 - 블로그: https://standout.tistory.com/1663

DAY04 상세기록 - 깃: https://github.com/StandOut-0/Study-AI/commits/day4

## 📂 프로젝트 구조
제공된 가이드라인에 따라 다음과 같이 디렉토리 및 파일을 구성하였습니다.
- `.venv`: 가상 환경
- `main.py`: 프로그램 메인 실행 파일 및 메뉴 제어
- `loop/while_mission.py`: 리스트 활용 성적 관리 프로그램
- `fileio/fileio_mission.py`: 딕셔너리 및 파일 I/O 활용 직원 관리 서비스

---

## 🚀 실행 흐름 (main.py)
프로그램 시작 시 `menu()` 함수가 실행되며, `while` 루프를 통해 아래 프롬프트가 반복 출력됩니다.
1. **while 실습문제**: 성적 관리 서비스 실행
2. **fileio 실습문제**: 직원 정보 관리 서비스 실행
3. **과제 실행 테스트 끝내기**: 전체 프로그램 종료

---

## 📝 상세 요구사항 및 구현 내용

### 1. 성적 관리 프로그램 (`loop/while_mission.py`)
- **함수명**: `sungjuk_process()`
- **데이터 구조**: `sungjuk_list` (초기 데이터: 홍길동, 김유신, 황지니)
- **주요 기능**:
  - **추가 (1)**: 번호(int), 이름(str), 점수(int)를 입력받아 리스트에 추가합니다.
  - **삭제 (2)**: 리스트의 특정 인덱스 순번을 입력받아 아이템을 제거합니다. 
    - 잘못된 인덱스 입력 시 예외 메시지(`순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.`)를 출력합니다.
  - **출력 (3)**: 저장된 리스트 정보를 인덱스와 함께 한 줄씩 출력합니다.
  - **종료 (4)**: 루프를 종료하고 "성적관리 프로그램이 종료되었습니다."를 출력합니다.

### 2. 직원 정보 관리 서비스 (`fileio/fileio_mission.py`)
- **함수명**: `emp_process()`
- **데이터 구조**: `emp_dict` (Key: 사번, Value: 직원 정보 리스트)
- **주요 기능**:
  - **새 직원정보 추가 (1)**: 사번, 이름, 주민번호, 이메일, 전화번호, 급여, 직급, 부서를 입력받아 딕셔너리에 저장합니다.
  - **직원정보 삭제 (2)**: 삭제할 사번을 입력받아 해당 데이터를 제거하고 안내 메시지를 출력합니다.
  - **전체 출력 (3)**: 딕셔너리에 저장된 모든 정보를 한 줄씩 출력합니다.
  - **파일에 저장 (4)**: `employees.dat` 파일에 딕셔너리 객체 상태 그대로 저장합니다.
  - **파일로부터 읽어오기 (5)**: `employees.dat` 파일을 읽어 `emp_dict`에 복원하고 내용을 출력합니다.
  - **서비스 끝내기 (9)**: 루프를 종료하고 "직원 관리 프로그램을 종료합니다."를 출력합니다.

---


프로그램 종
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/61bda23f-3c7d-4a82-837a-e90dd8975858" />
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/f727fdf3-9702-4984-9a22-9be0976e350d" />

서비스 진입
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/82f0f2b3-eee3-4d0c-8149-10d594a76cbf" />

추가 테스트
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/22281896-c86c-4e97-a68a-6253580ff18e" />

삭제 테스트
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/c6999e5b-d423-4038-8bb2-730c349c0e88" />

while 프로그램 종료
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/a84f3d09-d4da-4c74-8e21-d852eb667831" />

서비스 진입
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/043ba4ed-6e7c-4072-bb8b-35e739c4efc6" />

데이터 입력
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/508ccade-be8d-42fb-9db5-79dd955045a4" />

데이터 삭제
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/be3987e4-e9c2-4710-8b84-b72365d551b9" />

데이터 출력
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/2471b9b9-18eb-485d-a10f-09c5b964282d" />

데이터 저장
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/19d739d3-c2fe-4c3a-9fbf-546e7b9f862f" />

파일읽기, 서비스 끝내기, 서비스 끝내기
<img width="1280" height="870" alt="image" src="https://github.com/user-attachments/assets/2aa0de2d-b100-4c67-baee-3f8a4396bf75" />


완료.
