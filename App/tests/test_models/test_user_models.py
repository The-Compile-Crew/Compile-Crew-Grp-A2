import unittest
from App.models import User
from werkzeug.security import check_password_hash

class UserModelUnitTests(unittest.TestCase):

    def test_create_user(self):
        user = User("alice", "securepass")
        self.assertEqual(user.username, "alice")
        self.assertNotEqual(user.password, "securepass")  # Password should be hashed

    def test_check_password(self):
        user = User("alice", "securepass")
        self.assertTrue(user.check_password("securepass"))
        self.assertFalse(user.check_password("wrongpass"))

    def test_get_json(self):
        user = User("alice", "securepass")
        expected = {'id': None, 'username': 'alice'}
        self.assertDictEqual(user.get_json(), expected)

    def test_password_hashing(self):
        raw_password = "securepass"
        user = User("alice", raw_password)
        self.assertTrue(check_password_hash(user.password, raw_password))
