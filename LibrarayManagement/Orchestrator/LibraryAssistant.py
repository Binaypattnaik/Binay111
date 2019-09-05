from StudentManager import StudentManager
class LibraryAssistant:
    def __init__(self):
        self.student_manager = StudentManager()
    def invoke_student_manager(self):
        try:
            self.student_manager.register_student()
        except Exception as e:
            print(e.message, e)

if __name__ == "__main__":
    library_assistant = LibraryAssistant()
    library_assistant.invoke_student_manager()