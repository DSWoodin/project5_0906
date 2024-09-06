class Student:
    def __init__(self, name, contact, email):
        self.name = name
        self.contact = contact
        self.email = email

    def update_info(self, contact=None, email=None):
        if contact:
            self.contact = contact
        if email:
            self.email = email

    def __str__(self):
        return (f"이름: {self.name}\n"
                f"연락처: {self.contact}\n"
                f"이메일: {self.email}")

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, contact, email):
        if name in self.students:
            print(f"{name} 학생 정보는 이미 존재합니다.")
        else:
            self.students[name] = Student(name, contact, email)
            print(f"{name} 학생 정보를 추가했습니다.")

    def get_student(self, name):
        if name in self.students:
            return self.students[name]
        else:
            return "정보를 조회할 수 없습니다."

    def update_student(self, name, contact=None, email=None):
        student = self.get_student(name)
        if isinstance(student, Student):
            student.update_info(contact, email)
            print(f"{name} 학생 정보가 수정되었습니다.")
        else:
            print(student)

    def print_all_students(self):
        if not self.students:
            print("저장된 학생 정보가 없습니다.")
        else:
            for student in self.students.values():
                print(student)
                print("-----")

# 메인 코드 실행 부분
if __name__ == "__main__":
    manager = StudentManager()

    while True:
        print("1. 학생 추가")
        print("2. 학생 정보 조회")
        print("3. 학생 정보 수정")
        print("4. 모든 학생 정보 보기")
        print("5. 종료")
        
        choice = input("원하는 작업의 번호를 선택하세요: ")
        
        if choice == "1":
            name = input("학생 이름을 입력하세요: ")
            contact = input("연락처를 입력하세요: ")
            email = input("이메일을 입력하세요: ")
            manager.add_student(name, contact, email)
        
        elif choice == "2":
            name = input("조회할 학생의 이름을 입력하세요: ")
            student = manager.get_student(name)
            if isinstance(student, Student):
                print("학생 정보 조회:")
                print(student)
            else:
                print(student)
        
        elif choice == "3":
            name = input("수정할 학생의 이름을 입력하세요: ")
            contact = input("새 연락처를 입력하세요 (변경하지 않으려면 Enter를 누르세요): ")
            email = input("새 이메일을 입력하세요 (변경하지 않으려면 Enter를 누르세요): ")
            # 빈 문자열이 입력된 경우, 수정하지 않음
            if contact == "":
                contact = None
            if email == "":
                email = None
            manager.update_student(name, contact, email)
        
        elif choice == "4":
            print("\n모든 학생 정보:")
            manager.print_all_students()
        
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")


class Student:
    def __init__(self, name, contact, email):
        self.name = name
        self.contact = contact
        self.email = email
        self.department = None  # 학과 정보는 처음에는 없음

    def update_info(self, contact=None, email=None, department=None):
        if contact:
            self.contact = contact
        if email:
            self.email = email
        if department:
            self.department = department

    def __str__(self):
        department_info = self.department if self.department else "학과 정보 없음"
        return (f"이름: {self.name}\n"
                f"연락처: {self.contact}\n"
                f"이메일: {self.email}\n"
                f"학과: {department_info}")

class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, contact, email):
        if name in self.students:
            print(f"{name} 학생 정보는 이미 존재합니다.")
        else:
            self.students[name] = Student(name, contact, email)
            print(f"{name} 학생 정보를 추가했습니다.")

    def get_student(self, name):
        if name in self.students:
            return self.students[name]
        else:
            return "정보를 조회할 수 없습니다."

    def update_student(self, name, contact=None, email=None, department=None):
        student = self.get_student(name)
        if isinstance(student, Student):
            student.update_info(contact, email, department)
            print(f"{name} 학생 정보가 수정되었습니다.")
        else:
            print(student)

    def print_all_students(self):
        if not self.students:
            print("저장된 학생 정보가 없습니다.")
        else:
            for student in self.students.values():
                print(student)
                print("-----")

# 메인 코드 실행 부분
if __name__ == "__main__":
    manager = StudentManager()

    while True:
        print("1. 학생 추가")
        print("2. 학생 정보 조회")
        print("3. 학생 정보 수정")
        print("4. 모든 학생 정보 보기")
        print("5. 종료")
        
        choice = input("원하는 작업의 번호를 선택하세요: ")
        
        if choice == "1":
            name = input("학생 이름을 입력하세요: ")
            contact = input("연락처를 입력하세요: ")
            email = input("이메일을 입력하세요: ")
            manager.add_student(name, contact, email)
        
        elif choice == "2":
            name = input("조회할 학생의 이름을 입력하세요: ")
            student = manager.get_student(name)
            if isinstance(student, Student):
                print("학생 정보 조회:")
                print(student)
            else:
                print(student)
        
        elif choice == "3":
            name = input("수정할 학생의 이름을 입력하세요: ")
            contact = input("새 연락처를 입력하세요 (변경하지 않으려면 Enter를 누르세요): ")
            email = input("새 이메일을 입력하세요 (변경하지 않으려면 Enter를 누르세요): ")
            department = input("새 학과를 입력하세요 (변경하지 않으려면 Enter를 누르세요): ")
            # 빈 문자열이 입력된 경우, 수정하지 않음
            if contact == "":
                contact = None
            if email == "":
                email = None
            if department == "":
                department = None
            manager.update_student(name, contact, email, department)
        
        elif choice == "4":
            print("\n모든 학생 정보:")
            manager.print_all_students()
        
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
