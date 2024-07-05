import psycopg2
import os

class DbConnection:
    """
    Implements a singleton pattern
    """
    _instance = None # only for use within this class
    
    def __new__(cls):
        """
        Implements a single global connection to a database
        """
        if cls._instance is None:
            cls._instance = super(DbConnection, cls).__new__(cls)
            cls._instance.conn = cls._instance.connect()
        
        return cls._instance
    
    
    def connect(self):
        """
        Creates a connection to the databse

        Returns:
            psycopg2.extensions.connection: connection to the database
        """
        try:
            conn = psycopg2.connect(
                dbname=os.environ['DB_NAME'],
                user=os.environ['DB_USER'],
                password=os.environ['DB_PASSWORD'],
                host=os.environ['DB_HOST'],
                port=os.environ['DB_PORT']
            )
            return conn
        
        except psycopg2.Error as e:
            print(f"Error connecting to database: {e}")
            return None
    
    def get_connection(self):
        """
        Get the current connection of the database and if not connected
        connect to the db

        Returns:
            psycopg2.extensions.connection: database connection
        """
        if self.conn != 0 or self.conn is None:
            self.conn = self.connect()
        return self.conn

    def close_connection(self):
        """
        Closes the database connection
        """
        if self.conn is not None and self.conn.closed == 0:
            self.conn.close()