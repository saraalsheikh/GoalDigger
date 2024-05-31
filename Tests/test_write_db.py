import mysql.connector
from unittest.mock import MagicMock
import unittest
from model_write_db import Write_db

class TestWriteDbNewMethods(unittest.TestCase):
    def setUp(self):
        """Set up the test case."""
        self.write_db = Write_db()

    def test_insert_new_user(self):
        """Test the insert_new_user method."""
        user_id = "12345"
        username = "testuser"
        password = "testpassword"
        
        # Mock the database connection and cursor
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        self.write_db.mydb = mock_db
        self.write_db.mycursor = mock_cursor
        
        # Call the method
        self.write_db.insert_new_user(user_id, username, password)
        
        # Check if the correct SQL query was executed
        mock_cursor.execute.assert_called_once_with(
            f"INSERT INTO user_info (user_id, user_name, password) Values('{user_id}', '{username}', '{password}')"
        )
        mock_db.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_db.close.assert_called_once()

    def test_insert_plan(self):
        """Test the insert_plan method."""
        plan = ("Test plan", "2024-01-01", "12345")
        plan_text, plan_date, user_id = plan
        
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        self.write_db.mydb = mock_db
        self.write_db.mycursor = mock_cursor
        
        self.write_db.insert_plan(plan)
        
        mock_cursor.execute.assert_called_once_with(
            f"INSERT INTO to_do_list ( user_id, plan_text, plan_date) VALUES ('{user_id}', '{plan_text}', '{plan_date}')"
        )
        mock_db.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_db.close.assert_called_once()

    def test_insert_mood(self):
        """Test the insert_mood method."""
        user_mood = "happy"
        user_id = "12345"
        current_datetime = "2024-01-01 12:00:00"
        
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        self.write_db.mydb = mock_db
        self.write_db.mycursor = mock_cursor
        
        self.write_db.insert_mood(user_mood, user_id, current_datetime)
        
        mock_cursor.execute.assert_called_once_with(
            f"INSERT INTO mood (user_id, user_mood, mood_date) VALUES ('{user_id}', '{user_mood}', '{current_datetime}')"
        )
        mock_db.commit.assert_called_once()
        mock_cursor.close.assert_called_once()
        mock_db.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()
