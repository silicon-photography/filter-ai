import unittest
import os
import sys
sys.path.append(os.getcwd())

from backend.app.database.db_connection import DbConnection

class TestDbConnection(unittest.TestCase):
    
    def test_singleton(self):
        """
        Tests the singleton pattern of the database
        """
        db1 = DbConnection()
        db2 = DbConnection()
        self.assertIs(db1, db2)
        
    def test_connect(self):
        """
        Tests the connection of the database
        """
        db1 = DbConnection()
        conn = db1.get_connection()
        self.assertEqual(conn.closed, 0)
        
    def test_close(self):
        """
        Tests the closing of the database
        """
        db1 = DbConnection()
        db1.close_connection()
        self.assertEqual(db1.conn.closed, 1)
        

if __name__ == '__main__':
    unittest.main()