from DataBaseInteractor.DataBaseUtil import DataBaseUtil
from DataBaseInteractor.QueryConstants import \
    queries
from Exceptions.DataLayerException import DataLayerException
class StudentDAO:
    def __init__(self):
       self.db_object = DataBaseUtil()
    def insert_student_details(self, studentDTO):
        db_connection = self.db_object \
            .get_data_base_connection()
        try:
            sql_query = \
                queries.insert_into_student % (studentDTO.name, studentDTO.id,studentDTO.gender)
            print(sql_query)
            cursor = db_connection.cursor()
            cursor.execute(sql_query)
            db_connection.commit()
        except Exception as e:
            raise DataLayerException(e.args)
        finally:
            self.db_object.close_data_base_connection(db_connection)
    def update_student_details(self, studentDTO):
        pass
    def get_student_details(self, studentId):
        pass