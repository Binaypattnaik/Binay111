from DataBaseInteractor.DTO.studentDTO import studentDTO
from DataBaseInteractor.DAO.StudentDAO import StudentDAO
class StudentManager:
    def __init__(self):
        self.studentDAO = StudentDAO()
    def register_student(self):
        try:
            studentDTO = \
                self.get_student_details_console()
            print("calling student DAO")
            self.studentDAO.insert_student_details(studentDTO)
            print("Registered student "
                  "successfully")
        except Exception as e:
            raise e

    def get_student_details_console(self):
        name = raw_input("Enter the sudent "
                         "name: ")
        id = int(raw_input("Enter the student "
                          "Id: "))
        gender = raw_input("Enter the gender: ")
        return studentDTO(name, id, gender)