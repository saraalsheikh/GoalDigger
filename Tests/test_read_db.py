import mysql.connector
from unittest.mock import MagicMock, patch
import unittest
from model.read_db import Read_db

class TestReadDb(unittest.TestCase):
    """Test the Read_db class."""

    def setUp(self):
        """Set up the test case."""
        self.read_db = Read_db()

    def test_init(self):
        """Test the __init__ method."""
        self.assertIsInstance(self.read_db, Read_db)

    def test_open_db(self):
        """Test the open_db method."""
        with patch('mysql.connector.connect') as mock_connect:
            mock_db = MagicMock()
            mock_connect.return_value = mock_db
            self.read_db.open_db()
            mock_connect.assert_called_once()
            self.assertEqual(self.read_db.mydb, mock_db)
            self.assertIsInstance(self.read_db.mycursor, MagicMock)

    def test_close_db(self):
        """Test the close_db method."""
        mock_cursor = MagicMock()
        mock_db = MagicMock()
        self.read_db.mydb = mock_db
        self.read_db.mycursor = mock_cursor
        self.read_db.close_db()
        mock_cursor.close.assert_called_once()
        mock_db.close.assert_called_once()

    def test_get_user_info(self):
        """Test the get_user_info method."""
        mock_data = [("1", "user1", "password1")]
        self.read_db.mycursor = MagicMock()
        self.read_db.mycursor.fetchall.return_value = mock_data

        user_info_list = self.read_db.get_user_info("1")
        self.read_db.mycursor.execute.assert_called_with("SELECT * From user_info Where user_id = '1';")
        self.assertEqual(user_info_list, ["1", "user1", "password1"])

    def test_check_cridential(self):
        """Test the check_cridential method."""
        mock_data = ("1", "user1", "password1")
        self.read_db.mycursor = MagicMock()
        self.read_db.mycursor.fetchone.return_value = mock_data

        result = self.read_db.check_cridential("user1", "password1")
        self.read_db.mycursor.execute.assert_called_with("SELECT * FROM user_info WHERE user_name = 'user1' and password = 'password1';")
        self.assertTrue(result)

    def test_fetch_user_id(self):
        """Test the fetch_user_id method."""
        mock_data = ("1",)
        self.read_db.mycursor = MagicMock()
        self.read_db.mycursor.fetchone.return_value = mock_data

        user_id = self.read_db.fetch_user_id("user1")
        self.read_db.mycursor.execute.assert_called_with("SELECT user_id FROM user_info WHERE user_name = %s;", ("user1",))
        self.assertEqual(user_id, "1")

    def test_authenticate_user(self):
        """Test the authenticate_user method."""
        mock_data = [("1", "user1", "password1")]
        self.read_db.mycursor = MagicMock()
        self.read_db.mycursor.fetchall.return_value = mock_data

        result = self.read_db.authenticate_user("user1", "password1")
        self.read_db.mycursor.execute.assert_called_with("SELECT * FROM user_info WHERE user_name = 'user1' AND password = 'password1';")
        self.assertTrue(result)

    def test_fetch_plans(self):
        """Test the fetch_plans method."""
        mock_data = [("2023-01-01", "Plan 1"), ("2023-01-02", "Plan 2")]
        self.read_db.mycursor = MagicMock()
        self.read_db.mycursor.fetchall.return_value = mock_data

        plans = self.read_db.fetch_plans("1")
        self.read_db.mycursor.execute.assert_called_with("SELECT plan_date, plan_text FROM to_do_list WHERE user_id = '1';")
        self.assertEqual(plans, ["2023-01-01 Plan 1", "2023-01-02 Plan 2"])

    def test_fetch_mood(self):
        """Test the fetch_mood method."""
        mock_data = [("2023-01-01", "Happy"), ("2023-01-02", "Sad")]
        self.read_db.mycursor = MagicMock()
        self.read_db.mycursor.fetchall.return_value = mock_data

        moods = self.read_db.fetch_mood("1")
        self.read_db.mycursor.execute.assert_called_with("SELECT user_mood, mood_date FROM mood WHERE user_id = '1'")
        self.assertEqual(moods, ["2023-01-01 Happy", "2023-01-02 Sad"])

if __name__ == "__main__":
    unittest.main()
