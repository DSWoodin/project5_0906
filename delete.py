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

# 학생 정보 검색 및 삭제 기능 DELETE
def delete_student():
    name = input("삭제할 학생의 이름을 입력하세요: ")
    global students
    # 학생 리스트에서 해당 이름의 학생을 필터링하여 제거합니다.
    updated_students = [student for student in students if student.name != name]
    if len(updated_students) < len(students):  # 학생이 삭제되었는지 확인합니다.
        students = updated_students
        print(f"학생 {name}의 정보가 성공적으로 삭제되었습니다!\n")
    else:
        print("정보가 조회되지 않습니다.")  # 해당 학생이 없는 경우

# 학생 정보 검색 기능 SEARCH
def search_student():
    name = input("조회할 학생의 이름을 입력하세요: ")
    for student in students:
        if student.name == name:
            print("학생 정보 조회:")
            print(student)
            return
    print("정보가 조회되지 않습니다.")

def main(): # 이 함수는 py파일을 실행시키면 가장 먼저 작동합니다.
    while True: # 기본값이 True 이므로 while True: 이후의 코드는 무조건 작동합니다.
        print("\n## 작업 목록 ##")
        print("1. 신규 학생 추가") # "신규 학생 추가" 라는 메세지를 출력합니다.
        print("2. 학생 정보 조회")
        print("3. 학생 정보 삭제")
        print("4. 프로그램 종료") # "프로그램 종료" 라는 메세지를 출력합니다.
        choice = input("어떤 작업을 진행하시겠습니까? ") # "어떤 작업을 진행하시겠습니까?"를 출력하고 입력받는 숫자를 choice 변수에 저장합니다.
        
        if choice == '1':
            create_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못 입력하였습니다. 다시 입력해주세요")


if __name__ == "__main__": # 이 구문은 py파일이 직접 실행될때만 main() 함수가 실행되게끔 합니다.
    main()