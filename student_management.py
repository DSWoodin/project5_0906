"""
student_management.py 파일에서 진행된 작업은 아래와 같습니다.

1. create.py, update.py, delete.py 병합
2. 함수명 변경 search_student() -> read_student()
3. update_student()에서 이름 변경 기능 추가
4. 전체 주석 및 줄바꿈 스타일 통일

"""


# 학생정보를 저장하는 리스트
students = []

# 학생정보를 저장하는 클래스
class Student:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.department = None  # 추가적인 학과 정보는 나중에 업데이트 가능

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Department: {self.department}"

# CREATE: 학생의 이름, 전화번호, 이메일을 신규 등록하는 함수
def create_student(): # 이 함수는 main()에 의해 '1' 입력 시 작동
    name = input("\n학생 이름을 입력하세요: ") 
    phone = input("\n학생 전화번호를 입력하세요: ") 
    email = input("\n학생 이메일을 입력하세요: ")
    
    new_student = Student(name, phone, email) # 학생 정보를 Student 클래스를 이용해 new_student에 저장
    students.append(new_student) # students 변수에 new_student 정보를 append
    print(f"\n학생 {name}의 기본 정보가 등록되었습니다!")

# ADD: 등록된 학생 이름을 입력하면 학생의 새로운 정보를 등록하는 함수
def add_student(): # 이 함수는 main()에 의해 '2' 입력 시 작동
    name = input("\n추가 정보를 입력할 학생 이름을 입력하세요: ")
    for student in students:
        if student.name == name:
            department = input(f"\n{name}의 학과를 입력하세요: ")
            student.department = department
            print(f"\n{name}의 학과 정보가 추가되었습니다!")
            return
    print(f"\n학생 {name}의 정보가 조회되지 않습니다.") # 해당 학생이 없는 경우

# UPDATE: 등록된 학생 이름을 입력하면 학생의 정보를 수정하는 함수
def update_student(): # 이 함수는 main()에 의해 '3' 입력 시 작동
    name = input("\n수정할 학생의 이름을 입력하세요: ")
    for student in students:
        if student.name == name:
            print(f"\n수정 대상 학생 정보")
            print(f"{student}")
            print("\n수정할 정보를 선택하세요:")
            print("1. 이름")
            print("2. 전화번호")
            print("3. 이메일")
            print("4. 학과")
            print("5. 모두 수정")
            choice = input("선택 (1/2/3/4/5): ")

            if choice == '1':  # 이름 수정
                new_name = input(f"\n새로운 이름을 입력하세요 (현재 이름: {student.name}): ")
                if new_name:
                    student.name = new_name
                    print(f"\n{name}의 이름이 성공적으로 {new_name}으로 수정되었습니다!")

            elif choice == '2':  # 전화번호 수정
                phone = input(f"\n새로운 전화번호를 입력하세요 (현재 번호: {student.phone}): ")
                if phone:
                    student.phone = phone
                    print(f"\n{name}의 전화번호가 성공적으로 수정되었습니다!")
            
            elif choice == '3':  # 이메일 수정
                email = input(f"\n새로운 이메일을 입력하세요 (현재 이메일: {student.email}): ")
                if email:
                    student.email = email
                    print(f"\n{name}의 이메일이 성공적으로 수정되었습니다!")
            
            elif choice == '4':  # 학과 수정
                department = input(f"\n새로운 학과를 입력하세요 (현재 학과: {student.department}): ")
                if department:
                    student.department = department
                    print(f"\n{name}의 학과가 성공적으로 수정되었습니다!")
            
            elif choice == '5':  # 모든 정보 수정
                new_name = input(f"\n새로운 이름을 입력하세요 (현재 이름: {student.name}): ")
                phone = input(f"\n새로운 전화번호를 입력하세요 (현재 번호: {student.phone}): ")
                email = input(f"\n새로운 이메일을 입력하세요 (현재 이메일: {student.email}): ")
                department = input(f"\n새로운 학과를 입력하세요 (현재 학과: {student.department}): ")

                if new_name:
                    student.name = new_name
                if phone:
                    student.phone = phone
                if email:
                    student.email = email
                if department:
                    student.department = department
                
                print(f"\n{name}의 모든 정보가 성공적으로 수정되었습니다!")
            
            else:
                print("\n잘못된 선택입니다. 다시 시도하세요.")
            return
               
    print(f"\n학생 {name}의 정보가 조회되지 않습니다.") # 해당 학생이 없는 경우

# READ: 등록된 학생 이름을 입력하면 학생의 정보를 조회하는 함수
def read_student(): # 이 함수는 main()에 의해 '4' 입력 시 작동
    name = input("\n조회할 학생의 이름을 입력하세요: ")
    for student in students:
        if student.name == name:
            print("\n학생 정보 조회 결과")
            print(student)
            return
    print(f"\n학생 {name}의 정보가 조회되지 않습니다.") # 해당 학생이 없는 경우

# DELETE: 등록된 학생 이름을 입력하면 학생의 정보를 삭제하는 함수
def delete_student(): # 이 함수는 main()에 의해 '5' 입력 시 작동
    name = input("\n삭제할 학생의 이름을 입력하세요: ")
    global students
    updated_students = [student for student in students if student.name != name] # 학생 리스트에서 해당 이름의 학생을 필터링하여 삭제

    if len(updated_students) < len(students): # 학생이 삭제되었는지 확인
        students = updated_students
        print(f"\n학생 {name}의 정보가 성공적으로 삭제되었습니다!") # 학생 정보가 삭제되었음을 출력
    else: 
        print(f"\n학생 {name}의 정보가 조회되지 않습니다.") # 해당 학생이 없는 경우

def main(): # 이 함수는 py파일을 실행시키면 가장 먼저 작동합니다.
    while True:
        print("\n------------------------------")
        print("## 작업 목록 ##") # 가능한 작업 목록 리스트를 출력
        print("1. 학생 추가") 
        print("2. 학생 정보 추가") 
        print("3. 학생 정보 수정") 
        print("4. 학생 정보 조회")
        print("5. 학생 삭제")
        print("6. 프로그램 종료") 
        choice = input("어떤 작업을 진행하시겠습니까? ") # 진행할 작업의 번호를 입력받습니다.
        
        if choice == '1': # '1' 입력하면 create_student() 실행
            create_student() 
        elif choice == '2': # '2' 입력하면 add_student() 실행
            add_student() 
        elif choice == '3': # '3' 입력하면 update_student() 실행
            update_student() 
        elif choice == '4': # '4' 입력하면 read_student() 실행
            read_student()
        elif choice == '5': # '5' 입력하면 delete_student() 실행
            delete_student() 
        elif choice == '6': # '6' 입력하면 프로그램 종료
            break
        else: # 1~6 외의 것을 입력하면 잘못 입력했음을 알려주고 다시 입력하게 합니다.
            print("\n잘못 입력하였습니다. 다시 입력해주세요")

if __name__ == "__main__": # 이 구문은 py파일이 직접 실행될때만 main() 함수가 실행되게끔 합니다.
    main()