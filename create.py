# 학생정보를 저장할 리스트
students = []

# 학생정보를 저장할 클래스
class Student:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.department = None  # 추가적인 학과 정보는 나중에 업데이트 가능

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Department: {self.department}"

# 학생 정보 입력 및 저장 기능 CREATE
def create_student(): # 이 함수는 main()에 의해 '1'을 입력하면 작동됩니다.
    name = input("학생 이름을 입력하세요: ") # "학생 이름을 입력하세요:" 라는 문구를 출력하고, 학생 이름을 입력 받아서 name 변수에 저장합니다.
    phone = input("학생 전화번호를 입력하세요: ") # "학생 전화번호를 입력하세요:" 라는 문구를 출력하고, 학생 전화번호를 입력 받아서 phone 변수에 저장합니다.
    email = input("학생 이메일을 입력하세요: ") # "학생 이메일을 입력하세요:" 라는 문구를 출력하고, 학생 이메일을 입력 받아서 email 변수에 저장합니다.
    
    new_student = Student(name, phone, email) # name, phone, email 변수들에 저장된 학생 정보를 Student 클래스를 이용해 new_student 변수로 저장합니다.
    students.append(new_student) # students 변수에 new_student 정보를 append 합니다.
    print(f"학생 {name}의 정보가 성공적으로 추가되었습니다!\n") # 학생 정보를 모두 입력받으면 "학생 {이름}의 정보가 성공적으로 추가되었습니다!" 를 출력합니다.

def main(): # 이 함수는 py파일을 실행시키면 가장 먼저 작동합니다.
    while True: # 기본값이 True 이므로 while True: 이후의 코드는 무조건 작동합니다.
        print("\n## 작업 목록 ##")
        print("1. 신규 학생 추가") # "신규 학생 추가" 라는 메세지를 출력합니다.
        print("2. 프로그램 종료") # "프로그램 종료" 라는 메세지를 출력합니다.
        choice = input("어떤 작업을 진행하시겠습니까? ") # "어떤 작업을 진행하시겠습니까?"를 출력하고 입력받는 숫자를 choice 변수에 저장합니다.
        
        if choice == '1': # '1'를 입력하였다면
            create_student() # create_student() 함수를 실행시킵니다.
        elif choice == '2': # '2'를 입력하였다면 
            break # 프로그램을 종료시킵니다.
        else: # '1'이나 '2'가 아닌 외의 것을 입력하였다면
            print("잘못 입력하였습니다. 다시 입력해주세요") # 잘못 입력했음을 알려주고 다시 입력하게 합니다.

if __name__ == "__main__": # 이 구문은 py파일이 직접 실행될때만 main() 함수가 실행되게끔 합니다.
    main()