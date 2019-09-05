import MySQLdb;

class DataBaseUtil:
    def __init__(self):
        pass
    def get_data_base_connection(self):
        try:
            db_connection = MySQLdb.connect(
                "localhost","kick", "kick",
                "Librarysystem")
            return db_connection
        except Exception as e:
            raise e
    def close_data_base_connection(self, bd_connect):
        try:
            bd_connect.close()
        except Exception as e:
            raise e