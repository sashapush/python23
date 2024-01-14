#context manager to setup and teardown DB connection
import sqlite3

class DatabaseConnection:
    def __init__(self,host):
        self.connection = None #in order to use connection in both setup and teardown methods
        self.host = host
    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb: #means if exc_type is not None etc
            self.connection.close() #close connection without commiting if any error is observed
        else:
            self.connection.commit()
            self.connection.close()
